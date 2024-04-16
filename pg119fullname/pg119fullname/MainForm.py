import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.MediumOrchid
		self._textBox1.Location = System.Drawing.Point(269, 44)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(160, 33)
		self._textBox1.TabIndex = 0
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.MediumOrchid
		self._textBox2.Location = System.Drawing.Point(269, 107)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(160, 33)
		self._textBox2.TabIndex = 1
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		self._textBox2.TextChanged += self.TextBox2TextChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.GhostWhite
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.MediumOrchid
		self._label1.Location = System.Drawing.Point(22, 44)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(230, 33)
		self._label1.TabIndex = 2
		self._label1.Text = "Enter your first name:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.GhostWhite
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.MediumOrchid
		self._label2.Location = System.Drawing.Point(22, 106)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(230, 33)
		self._label2.TabIndex = 3
		self._label2.Text = "Enter your last name:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.GhostWhite
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.MediumOrchid
		self._label3.Location = System.Drawing.Point(22, 198)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(230, 33)
		self._label3.TabIndex = 4
		self._label3.Text = "This is your full name:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Thistle
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MediumOrchid
		self._button1.Location = System.Drawing.Point(22, 257)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(155, 82)
		self._button1.TabIndex = 6
		self._button1.Text = "show name"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Thistle
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MediumOrchid
		self._button2.Location = System.Drawing.Point(205, 257)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(155, 82)
		self._button2.TabIndex = 7
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Thistle
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MediumOrchid
		self._button3.Location = System.Drawing.Point(386, 257)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(155, 82)
		self._button3.TabIndex = 8
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.GhostWhite
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.MediumOrchid
		self._label4.Location = System.Drawing.Point(269, 198)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(284, 33)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Thistle
		self.ClientSize = System.Drawing.Size(565, 362)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "pg119fullname"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox2TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		firstname = str(self._textBox1.Text)
		lastname = str(self._textBox2.Text)
		fullname = firstname + " " + lastname
		self._label4.Text = fullname
		

	def Button3Click(self, sender, e):
		Application.Exit()
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""