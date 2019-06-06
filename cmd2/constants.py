#
# coding=utf-8
"""Constants and definitions"""
import re
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Used for command parsing, output redirection, tab completion and word
# breaks. Do not change.
QUOTES = ['"', "'"]
REDIRECTION_PIPE = '|'
REDIRECTION_OUTPUT = '>'
REDIRECTION_APPEND = '>>'
REDIRECTION_CHARS = [REDIRECTION_PIPE, REDIRECTION_OUTPUT]
REDIRECTION_TOKENS = [REDIRECTION_PIPE, REDIRECTION_OUTPUT, REDIRECTION_APPEND]
COMMENT_CHAR = '#'
MULTILINE_TERMINATOR = ';'

# Regular expression to match ANSI escape codes
ANSI_ESCAPE_RE = re.compile(r'\x1b[^m]*m')

LINE_FEED = '\n'

# values for colors setting
COLORS_NEVER = 'Never'
COLORS_TERMINAL = 'Terminal'
COLORS_ALWAYS = 'Always'
