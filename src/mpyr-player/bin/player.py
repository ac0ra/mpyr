#!/bin/env python
#
___author__ = 'Adam Grigolato'
__version__ = '0'
#IMPORTS
#


class APIServerProtocol:
    '''Datagram Schemas
    Intial Packet # From Client
    {'p':'i','pk':'$public_key$','ph':'$public_hash$'}
    Initial Packet # From Server
    {'p':'ia','epk':'$session_key$','eph':'$session_hash$','esw':'$session_window'}


    '''
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        loop = asyncio.get_event_loop()
        loop.create_task(self.handle_income_packet(data, addr))

    async def handle_income_packet(self, data, addr):
        # reply message back (Testing)
        self.transport.sendto(data, addr)

    def pad(self,s):
        return s + ((16 - len(s) % 16) * '`')

    def depad(self,s):
        return s.replace('`','')

    def init_key(self,key):
        

    def packs(self,pubkey,content):

    def unpacks(self,pubkey,content):
        

    def cmd_add(self):

    def cmd_rm(self):

    def cmd_ls(self):


class MPyr_Player_Menu(object):

    def __init__(self):
        import argparse
        import sys
        parser = argparse.ArgumentParser(
            description='MPyr Player',
            usage='''mpyr player <command> [<args>]

The most commonly used player commands are:
   start         Start an MPyr instance.
   kill          Cleanup an old instance.
   config        Read / Modify server configuration.
''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def start(self):
        parser = argparse.ArgumentParser(description='Start an MPyr Instance')
        parser.add_argument('profile')
        args = parser.parse_args(sys.argv[2:])
        print('weee')

    def kill(self):
        pass

    def config(self):
        parser = argparse.ArgumentParser(description='Read / Modify server configuration.')
        parser.add_argument('--insert_argument_here')
        args = parser.parse_args(sys.argv[2:])
        print('weee')


class MPyr_server_instance():

    def __init__(self,args = False,config = False):
        import asyncio
        from mplayer.async import AsyncPlayer
        `rimport os
        from threading import Thread
        import logging
        import socket
        self.player = AsyncPlayer(autospawn=False)
        # Empty Playlist
        self.playlist = []
        if args:
            self.player.args = args
        else:
            # Set argument defaults
            self.player.args = ['-really-quiet', '-msglevel', 'global=6']
        if config:
           self.config = config
        else:
            `r# Set configuration defaults
            home = os.getenv("HOME")
            self.config['api_socket'] = home + '/.mpyr/api.sock'
            self.config['udp_port'] = 38472
            self.config['udp_enabled'] = True
            self.config['udp_host'] = '127.0.0.1'
        if self.config[udp_enable]:
            self.setup_udp()

    def setup_udp(self):
        # One protocol instance will be created to serve all
        # client requests.
        transport, protocol = await loop.create_datagram_endpoint(
        lambda: APIServerProtocol(),
        local_addr=(self.config['udp_host'], self.config['udp_port']))

    def handle_data(self,data):
        if not data.startswith('EOF code'):
            print('log: %s' % (data, ))
        else:
            self.player.quit()

    def connect_output(self):
        self.player.stdout.connect(self.handle_data)
        self.player.stderr.connect(self.log_error)

    def init_playlist(


    def spawn(self):
        self.player.spawn()

    def loadfile(self, file):
        self.player.loadfile(file)

    def log_error(self,msg):
        print('ERROR: {0}'.format(msg))

    def status(self,p):
        while p.is_alive():
            print('time_pos = {0}'.format(p.time_pos))
            time.sleep(1.0)
            self.status_quiet(p)

    def status_quiet(self,p):
        while p.is_alive():
            if self.mplayer_alive != p.is_alive():
                self.mplayer_alive = p.is_alive():

    def run_loop(self,debug):
        if debug:
            t = Thread(target=self.status, args=(self.player,))
        else:
            t=Thread(target=self.status_quiet args=(self.player,))
        t.daemon = True
        t.start()
        asyncore.loop()


if __name__ == '__main__':
    global server_lock = False
    global playlist = []
    global conn_list = {}
    MPyr_player_Menu()
    timer = 500
    instance = MPyr_server_instance()
    while timer > 0:
        


