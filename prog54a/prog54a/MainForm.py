import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(42, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(134, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Pick a car:"
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(202, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(134, 33)
		self._comboBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(42, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(134, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Miles:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(42, 99)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(134, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Gallons:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(42, 133)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(134, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "MPG:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label5.Location = System.Drawing.Point(202, 62)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(134, 23)
		self._label5.TabIndex = 5
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label6.Location = System.Drawing.Point(202, 133)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(134, 23)
		self._label6.TabIndex = 6
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._label7.Location = System.Drawing.Point(202, 99)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(134, 23)
		self._label7.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button1.Location = System.Drawing.Point(12, 171)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(174, 56)
		self._button1.TabIndex = 8
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Location = System.Drawing.Point(192, 171)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(180, 56)
		self._button2.TabIndex = 9
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button3.Location = System.Drawing.Point(12, 233)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(360, 58)
		self._button3.TabIndex = 10
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(384, 306)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog54a"
		self.ResumeLayout(False)


	def Label6Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		miles = 0
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286.0
			gallons = 9.0
		elif car == "1979 Firebird":
			miles = 412.0
			gallons = 40
		elif car == "1980 Subaru":
			miles = 361.0
			gallons = 18.0
		elif car == "1975 Cutlass":
			miles = 161.0
			gallons = 11.0
		# elif car == "second car":
			# miles = ...
			# gallons = ...
			
		mpg = miles / float(gallons)
		mpg = round(mpg, 1)
		
		self._label6.Text = str(mpg)
		self._label5.Text = str(miles)
		self._label7.Text = str(gallons)

	def Button1Click(self, sender, e):
		self._label6.Text = ""
		self._label7.Text = ""
		self._label5.Text = ""
		self._comboBox1.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()