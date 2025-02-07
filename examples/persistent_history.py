#!/usr/bin/env python
# coding=utf-8
"""This example demonstrates how to enable persistent readline history in your cmd2 application.

This will allow end users of your cmd2-based application to use the arrow keys and Ctrl+r in a manner which persists
across invocations of your cmd2 application.  This can make it much easier for them to use your application.
"""
import cmd2


class Cmd2PersistentHistory(cmd2.Cmd):
    """Basic example of how to enable persistent readline history within your cmd2 app."""
    def __init__(self, hist_file):
        """Configure the app to load persistent readline history from a file.

        :param hist_file: file to load readline history from at start and write it to at end
        """
        super().__init__(persistent_history_file=hist_file, persistent_history_length=500)
        self.allow_cli_args = False
        self.prompt = 'ph> '

    # ... your class code here ...


if __name__ == '__main__':
    import sys

    history_file = '~/.persistent_history.cmd2'
    if len(sys.argv) > 1:
        history_file = sys.argv[1]

    app = Cmd2PersistentHistory(hist_file=history_file)
    sys.exit(app.cmdloop())
