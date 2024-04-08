import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightCyan
		self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.Teal
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 21
		self._listBox1.Location = System.Drawing.Point(12, 15)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(571, 298)
		self._listBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCyan
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Teal
		self._label1.Location = System.Drawing.Point(77, 338)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 33)
		self._label1.TabIndex = 1
		self._label1.Text = "Guests:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightCyan
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Teal
		self._label2.Location = System.Drawing.Point(304, 338)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 33)
		self._label2.TabIndex = 2
		self._label2.Text = "Chairs:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightCyan
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.Teal
		self._textBox1.Location = System.Drawing.Point(183, 338)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 33)
		self._textBox1.TabIndex = 3
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightCyan
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.Teal
		self._textBox2.Location = System.Drawing.Point(410, 338)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 33)
		self._textBox2.TabIndex = 4
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightBlue
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.CadetBlue
		self._button1.Location = System.Drawing.Point(-3, 387)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(195, 68)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightBlue
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.CadetBlue
		self._button2.Location = System.Drawing.Point(198, 387)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(195, 68)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightBlue
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.CadetBlue
		self._button3.Location = System.Drawing.Point(399, 387)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(195, 68)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightBlue
		self.ClientSize = System.Drawing.Size(596, 464)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		heading = "Dinner Party"
		self._listBox1.Items.Add(heading)
		guests = int(self._textBox1.Text)
		chairs = int(self._textBox2.Text)
		Permutations = guests * 5 * 4 * 3
		People = guests - chairs
		heading2 = "Guests:" + "\t" + "Chairs:" + "\t" + "Permutations:" + "\t" + "People left standing"
		self._listBox1.Items.Add(heading2)
		msg = str(guests) + "\t" + str(chairs) + "\t" str(Permutations) + "\t" str(People)
		self._listBox1.Items.Add(msg)
	
