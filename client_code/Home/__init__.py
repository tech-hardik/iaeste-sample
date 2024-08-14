from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.pricing.search()

    # Any code you write here will run when the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
