# Enable-Motors
NO WARRANTY, AS IS, NO SUPPORT... unless you are nice


-- Farmware for farmbot --

Enable or Disable Motors Configuration - Keep Active


-- Do ---

execute config_update for params:
  movement_keep_active_x
  movement_keep_active_y
  movement_keep_active_z


-- input ---

  {"name": "movement_keep_active_x", "label": "Keep Active X Motors (1:enable 0:disable)", "value": 1}
  
-> X axis : 0 -> disable, 1 -> enable

  {"name": "movement_keep_active_y", "label": "Keep Active Y Motor (1:enable 0:disable)", "value": 1}
  
-> Y axis : 0 -> disable, 1 -> enable

  {"name": "movement_keep_active_z", "label": "Keep Active Z Motor (1:enable 0:disable)", "value": 1}
  
-> Z axis : 0 -> disable, 1 -> enable

  {"name": "debug", "label": "Debug (0-> No FW debug msg, 1-> FW debug msg)", "value": 1}
  
-> debug mode : 0 -> no farmware debug log, 1 -> farmware debug log


