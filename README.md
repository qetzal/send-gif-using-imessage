# Send random GIFs using iMessage

## Installation
Make sure you have Python and "requests" lib installed: http://docs.python-requests.org/en/latest/user/install/#install


## Usage

        usage: sendgif.py [-h] [-t TAG] to
        
        positional arguments:
          to                 Phone number or email that supports iMessage.
        
        optional arguments:
          -h, --help         show this help message and exit
          -t TAG, --tag TAG  Set Giphy tag. Default tag is 'cats'.


## Examples

`./sendgif.py -t kitten example@example.com`

`./sendgif.py -t "cute cats" +79270000000`
