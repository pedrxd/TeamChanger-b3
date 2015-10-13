#Team changer develop by pedrxd.

__version__ = '0.1'
__author__ = 'pedrxd'

import b3
import b3.events
import b3.plugin


class TeamchangerPlugin(b3.plugin.Plugin):
    requiresConfigFile = False
    def onStartup (self):
        self._adminPlugin = self.console.getPlugin('admin')
        
        if not self._adminPlugin:
            
            self.error('Could not find admin plugin')
            return
        
        self._adminPlugin.registerCommand(self, 'red', 20, self.red)
        self._adminPlugin.registerCommand(self, 'blue', 20, self.blue)
        self._adminPlugin.registerCommand(self, 'spec', 20, self.spec)
        
    def red(self, data, client, cmd):
        """Change a player team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
            
        self.console.write('forceteam %s red' % sclient.cid)
        sclient.message('Moved to red team')
            
    def blue(self, data, client, cmd):
        """Change a player team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
            
        self.console.write('forceteam %s blue' % sclient.cid)
        sclient.message('Moved to blue team')
            
    def spec(self, data, client, cmd):
        """Change a player team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
            
        self.console.write('forceteam %s spectator~~' % sclient.cid)
        sclient.message('Moved to spec')
            