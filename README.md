# lhf

Low-Hanging Fruit: A toolset for finding unsecured Raspberry Pis

### Overview

lhf uses Shodan to search for Internet-connected Raspberry Pis, then attempts to SSH into them with the default admin credentials (pi:raspberry).

On a default install of Raspbian, the pi user has full sudo access – so if you can log in, you basically have root.

Obligatory disclaimer: in the United States, it is illegal to log in to a remote machine without the owner's explicit consent. I offer lhf for learning purposes only. I am not responsible for your actions.

### Setup
I've only tested lhf on Linux, but it should work on Windows and ~~OS X~~ macOS with few changes, if any.

    git clone https://github.com/Fysac/lhf
    cd lhf && virtualenv .env && source .env/bin/activate
    pip install shodan paramiko

After the dependencies are installed, you just need to add your Shodan API Key:

    echo "YOUR KEY HERE" > SHODAN_API_KEY

### Usage

`find.py <max results=100>`

`scan.py <threads=10>`

In true Unix fashion, lhf operates entirely on standard streams. This means you can chain commands together like so:

    python find.py 500 | python scan.py 100 > owned_pies.txt

This command will find at most 500 Raspberry Pis, scan them all using 100 threads, and write the vulnerable host:port combos to a file.
