import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._listBox2 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(123, 278)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(267, 278)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(397, 277)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.AntiqueWhite
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(78, 98)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 95)
		self._listBox1.TabIndex = 3
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.Color.AntiqueWhite
		self._listBox2.FormattingEnabled = True
		self._listBox2.Location = System.Drawing.Point(352, 98)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(120, 95)
		self._listBox2.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CadetBlue
		self.ClientSize = System.Drawing.Size(619, 329)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "stadiumseating"
		self.ResumeLayout(False)

