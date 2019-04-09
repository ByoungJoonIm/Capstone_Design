# Dmoj judge

# judge.py : main

### judgeenv.load_env() : judgeenv.py

```python
def load_env(cli=False, testsuite=False):  # pragma: no cover
    global problem_dirs, only_executors, exclude_executors, log_file, server_host, \
        server_port, no_ansi, no_ansi_emu, env, startup_warnings, no_watchdog, \
        problem_regex, case_regex, api_listen, secure, no_cert_check, cert_store, \
        problem_watches, cli_command

    # dmoj - cli로 열기
    if cli:
        description = 'Starts a shell for interfacing with a local judge instance.'
    else:
        description = 'Spawns a judge for a submission server.'

    parser = argparse.ArgumentParser(description=description)

    # dmoj로 열기
    if not cli:
        parser.add_argument('server_host', help='host to connect for the server')
        parser.add_argument('judge_name', nargs='?', help='judge name (overrides configuration)')
        parser.add_argument('judge_key', nargs='?', help='judge key (overrides configuration)')
        parser.add_argument('-p', '--server-port', type=int, default=9999,
                            help='port to connect for the server')
    else:
        parser.add_argument('command', nargs='*', help='invoke CLI command without spawning shell')

    parser.add_argument('-c', '--config', type=str, default='~/.dmojrc',
                        help='file to load judge configurations from (default: ~/.dmojrc)')

    if not cli:
        parser.add_argument('-l', '--log-file',
                            help='log file to use')
        parser.add_argument('--no-watchdog', action='store_true',
                            help='disable use of watchdog on problem directories')
        parser.add_argument('-a', '--api-port', type=int, default=None,
                            help='port to listen for the judge API (do not expose to public, '
                                 'security is left as an exercise for the reverse proxy)')
        parser.add_argument('-A', '--api-host', default='127.0.0.1',
                            help='IPv4 address to listen for judge API')

        if ssl:
            parser.add_argument('-s', '--secure', action='store_true',
                                help='connect to server via TLS')
            parser.add_argument('-k', '--no-certificate-check', action='store_true',
                                help='do not check TLS certificate')
            parser.add_argument('-T', '--trusted-certificates', default=None,
                                help='use trusted certificate file instead of system')
        else:
            parser.set_defaults(secure=False, no_certificate_check=False, trusted_certificates=None)

    _group = parser.add_mutually_exclusive_group()
    _group.add_argument('-e', '--only-executors',
                        help='only listed executors will be loaded (comma-separated)')
    _group.add_argument('-x', '--exclude-executors',
                        help='prevent listed executors from loading (comma-separated)')

    parser.add_argument('--no-ansi', action='store_true', help='disable ANSI output')
    if os.name == 'nt':
        parser.add_argument('--no-ansi-emu', action='store_true', help='disable ANSI emulation on Windows')

    if testsuite:
        parser.add_argument('tests_dir', help='directory where tests are stored')
        parser.add_argument('problem_regex', help='when specified, only matched problems will be tested', nargs='?')
        parser.add_argument('case_regex', help='when specified, only matched cases will be tested', nargs='?')

    args = parser.parse_args()

    server_host = getattr(args, 'server_host', None)
    server_port = getattr(args, 'server_port', None)
    cli_command = getattr(args, 'command', [])

    no_ansi_emu = args.no_ansi_emu if os.name == 'nt' else True
    no_ansi = args.no_ansi
    no_watchdog = True if cli else args.no_watchdog
    if not cli:
        api_listen = (args.api_host, args.api_port) if args.api_port else None

        if ssl:
            secure = args.secure
            no_cert_check = args.no_certificate_check
            cert_store = args.trusted_certificates

    log_file = getattr(args, 'log_file', None)
    only_executors |= args.only_executors and set(args.only_executors.split(',')) or set()
    exclude_executors |= args.exclude_executors and set(args.exclude_executors.split(',')) or set()

    model_file = os.path.expanduser(args.config)

    with open(model_file) as init_file:
        env.update(yaml.safe_load(init_file))

        if getattr(args, 'judge_name', None):
            env['id'] = args.judge_name

        if getattr(args, 'judge_key', None):
            env['key'] = args.judge_key

        problem_dirs = env.problem_storage_root
        if problem_dirs is None:
            if not testsuite:
                raise SystemExit('problem_storage_root not specified in "%s"; '
                                 'no problems available to grade' % model_file)
        else:
            # Populate cache and send warnings
            get_problem_roots(warnings=True)

            problem_watches = []
            get_path = lambda x, y: utf8text(os.path.normpath(os.path.join(x, y)))
            for dir in problem_dirs:
                if isinstance(dir, ConfigNode):
                    for _, recursive_root in dir.iteritems():
                        problem_watches.append(get_path(_root, recursive_root))
                else:
                    problem_watches.append(get_path(_root, dir))

    if testsuite:
        if not os.path.isdir(args.tests_dir):
            raise SystemExit('Invalid tests directory')
        problem_dirs = [args.tests_dir]
        clear_problem_dirs_cache()

        import re
        if args.problem_regex:
            try:
                problem_regex = re.compile(args.problem_regex)
            except re.error:
                raise SystemExit('Invalid problem regex')
        if args.case_regex:
            try:
                case_regex = re.compile(args.case_regex)
            except re.error:
                raise SystemExit('Invalid case regex')
```
