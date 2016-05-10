# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 743,483 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_grid1 = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 60, 2 )
		self.m_grid1.EnableEditing( False )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 10, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 90 )
		self.m_grid1.SetColSize( 1, 60 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.SetRowSize( 0, 19 )
		self.m_grid1.SetRowSize( 1, 19 )
		self.m_grid1.SetRowSize( 2, 15 )
		self.m_grid1.SetRowSize( 3, 19 )
		self.m_grid1.SetRowSize( 4, 19 )
		self.m_grid1.AutoSizeRows()
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 30 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.m_grid1.SetLabelFont( wx.Font( 10, 74, 90, 90, False, "Century Gothic" ) )
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellFont( wx.Font( 11, 74, 90, 90, False, "Century Gothic" ) )
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.m_grid1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer6, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Program Counter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer71.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.pco = wx.StaticText( self.m_panel1, wx.ID_ANY, u"pc", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
		self.pco.Wrap( -1 )
		self.pco.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		self.pco.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.pco.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer71.Add( self.pco, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer61.Add( bSizer71, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Instrucción actual", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.inow = wx.StaticText( self.m_panel1, wx.ID_ANY, u"token", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_CENTRE )
		self.inow.Wrap( -1 )
		self.inow.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial" ) )
		self.inow.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.inow.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer8.Add( self.inow, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer61.Add( bSizer8, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer7.Add( bSizer61, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton2 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ICONO.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer18.Add( self.m_bpButton2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer18, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.titulo = wx.StaticText( self.m_panel1, wx.ID_ANY, u"SIMUSI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.titulo.Wrap( -1 )
		self.titulo.SetFont( wx.Font( 22, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.titulo.SetForegroundColour( wx.Colour( 70, 57, 234 ) )
		
		bSizer14.Add( self.titulo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer14, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.b_ejecutar = wx.Button( self.m_panel1, wx.ID_ANY, u"Ejecutar", wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.b_ejecutar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer13.Add( self.b_ejecutar, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer13, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer12, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Fuente (txt)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer9.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer9.Add( self.m_filePicker1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer9, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.b_load = wx.Button( self.m_panel1, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.b_load, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer11, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Velocidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer10.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self.m_panel1, wx.ID_ANY, 50, 1, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_SELRANGE|wx.SL_VERTICAL )
		bSizer10.Add( self.m_slider1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer10, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.SHAPED, 5 )
		
		
		bSizer7.Add( bSizer5, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer4 )
		self.m_panel1.Layout()
		bSizer4.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, 0, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
                # Connect Events
		self.b_load.Bind(wx.EVT_BUTTON, self.b_loaodOnButtonClick)
		self.b_ejecutar.Bind(wx.EVT_BUTTON, self.b_ejecutarOnButtonClick)
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def b_loaodOnButtonClick( self, event ):
		event.Skip()
	def b_ejecutarOnButtonClick( self, event ):
		event.Skip()
	

