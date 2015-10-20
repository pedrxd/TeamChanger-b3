#Team changer develop by pedrxd.

__version__ = '0.1'
__author__ = 'pedrxd'

import b3
import b3.events
import b3.plugin
import time


class TeamchangerPlugin(b3.plugin.Plugin):
    requiresConfigFile = False
            
    def setTeam(self, client, team):
        self.console.write('forceteam %s %s' % (client.cid, team))
    
    def onStartup (self):
        self._adminPlugin = self.console.getPlugin('admin')
        
        if not self._adminPlugin:
            
            self.error('Could not find admin plugin')
            return
        
        self._adminPlugin.registerCommand(self, 'red', 40, self.red)
        self._adminPlugin.registerCommand(self, 'blue', 40, self.blue)
        self._adminPlugin.registerCommand(self, 'spec', 40, self.spec)
        self._adminPlugin.registerCommand(self, 'replay', 40, self.replay, 'rp')
        self._adminPlugin.registerCommand(self, 'auto', 40, self.auto)
        
    def red(self, data, client, cmd):
        """Change a player team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
            
        self.setTeam(sclient, 'red')
        sclient.message('Moved to red team')
            
    def blue(self, data, client, cmd):
        """Change a player team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
           
        self.setTeam(sclient, 'blue') 
        sclient.message('Moved to blue team')
            
    def spec(self, data, client, cmd):
        """Change a player team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
            
        self.setTeam(sclient, 'spectator')
        sclient.message('Moved to spec')
        
    def replay(self, data, client, cmd):
        """Change to spec then rejoin to a team"""
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else:
            sclient = client
        
        lastteam = sclient.team
        self.setTeam(sclient, 'spectator')
        self.setTeam(sclient, '')
        sclient.message('Replay correctly')
        
    def auto(self, data, client, cmd):
        if data:
            sclient = self._adminPlugin.findClientPrompt(data, client)
            if not sclient: return
        else: 
            sclient = client
            
        self.setTeam(sclient, '')
        sclient.message('Correctly AutoJoin')
        