from racing.game.gameobject.gameobject import Event


class _Event(Event):

    def __init__(self, mdt):
        self.tsk = None
        Event.__init__(self, mdt)
        self.accept('p', eng.pause.logic.toggle)

    def start(self):
        self.tsk = taskMgr.add(self.__on_frame, 'Track::__on_frame')

    def __on_frame(self, task):
        cam_pos = eng.base.camera.get_pos()
        self.mdt.gfx.spot_lgt.setPos(cam_pos + (60, -60, 100))
        self.mdt.gfx.spot_lgt.lookAt(cam_pos + (-40, 60, -50))
        self.mdt.gui.update_minimap()
        return task.again

    def destroy(self):
        Event.destroy(self)
        taskMgr.remove(self.tsk)
