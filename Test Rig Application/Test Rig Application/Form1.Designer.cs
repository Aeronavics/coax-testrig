namespace Test_Rig_Application
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.portPanel = new System.Windows.Forms.Panel();
            this.portComboBox = new System.Windows.Forms.ComboBox();
            this.portLabel = new System.Windows.Forms.Label();
            this.connectButton = new System.Windows.Forms.Button();
            this.portPanelLabel = new System.Windows.Forms.Label();
            this.connectionsPanel = new System.Windows.Forms.Panel();
            this.temperatureSensorButton = new System.Windows.Forms.Button();
            this.bottomMotorButton = new System.Windows.Forms.Button();
            this.topMotorButton = new System.Windows.Forms.Button();
            this.connectionsPanelLabel = new System.Windows.Forms.Label();
            this.manualControlPanel = new System.Windows.Forms.Panel();
            this.throttleLabel = new System.Windows.Forms.Label();
            this.manualControlTrackBar = new System.Windows.Forms.TrackBar();
            this.manualArmButton = new System.Windows.Forms.Button();
            this.manualControlPanelLabel = new System.Windows.Forms.Label();
            this.autoTestStartButton = new System.Windows.Forms.Button();
            this.autoTestPanel = new System.Windows.Forms.Panel();
            this.autoTestPanelLabel = new System.Windows.Forms.Label();
            this.serialPort = new System.IO.Ports.SerialPort(this.components);
            this.portPanel.SuspendLayout();
            this.connectionsPanel.SuspendLayout();
            this.manualControlPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.manualControlTrackBar)).BeginInit();
            this.autoTestPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // portPanel
            // 
            this.portPanel.BackColor = System.Drawing.Color.White;
            this.portPanel.Controls.Add(this.portComboBox);
            this.portPanel.Controls.Add(this.portLabel);
            this.portPanel.Controls.Add(this.connectButton);
            this.portPanel.Controls.Add(this.portPanelLabel);
            this.portPanel.Location = new System.Drawing.Point(12, 12);
            this.portPanel.Name = "portPanel";
            this.portPanel.Size = new System.Drawing.Size(255, 114);
            this.portPanel.TabIndex = 0;
            // 
            // portComboBox
            // 
            this.portComboBox.FormattingEnabled = true;
            this.portComboBox.Location = new System.Drawing.Point(93, 42);
            this.portComboBox.Name = "portComboBox";
            this.portComboBox.Size = new System.Drawing.Size(121, 21);
            this.portComboBox.TabIndex = 7;
            this.portComboBox.SelectedIndexChanged += new System.EventHandler(this.portComboBox_SelectedIndexChanged);
            // 
            // portLabel
            // 
            this.portLabel.AutoSize = true;
            this.portLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.portLabel.Location = new System.Drawing.Point(31, 45);
            this.portLabel.Name = "portLabel";
            this.portLabel.Size = new System.Drawing.Size(38, 13);
            this.portLabel.TabIndex = 6;
            this.portLabel.Text = "Port :";
            // 
            // connectButton
            // 
            this.connectButton.BackColor = System.Drawing.Color.Green;
            this.connectButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.connectButton.Location = new System.Drawing.Point(54, 78);
            this.connectButton.Name = "connectButton";
            this.connectButton.Size = new System.Drawing.Size(146, 23);
            this.connectButton.TabIndex = 5;
            this.connectButton.Text = "Connect/Disconnect";
            this.connectButton.UseVisualStyleBackColor = false;
            this.connectButton.Click += new System.EventHandler(this.connectButton_Click);
            // 
            // portPanelLabel
            // 
            this.portPanelLabel.AutoSize = true;
            this.portPanelLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.portPanelLabel.Location = new System.Drawing.Point(101, 12);
            this.portPanelLabel.Name = "portPanelLabel";
            this.portPanelLabel.Size = new System.Drawing.Size(61, 13);
            this.portPanelLabel.TabIndex = 0;
            this.portPanelLabel.Text = "COM Port";
            // 
            // connectionsPanel
            // 
            this.connectionsPanel.BackColor = System.Drawing.Color.White;
            this.connectionsPanel.Controls.Add(this.temperatureSensorButton);
            this.connectionsPanel.Controls.Add(this.bottomMotorButton);
            this.connectionsPanel.Controls.Add(this.topMotorButton);
            this.connectionsPanel.Controls.Add(this.connectionsPanelLabel);
            this.connectionsPanel.Location = new System.Drawing.Point(12, 132);
            this.connectionsPanel.Name = "connectionsPanel";
            this.connectionsPanel.Size = new System.Drawing.Size(255, 123);
            this.connectionsPanel.TabIndex = 1;
            // 
            // temperatureSensorButton
            // 
            this.temperatureSensorButton.BackColor = System.Drawing.Color.Green;
            this.temperatureSensorButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.temperatureSensorButton.Location = new System.Drawing.Point(64, 90);
            this.temperatureSensorButton.Name = "temperatureSensorButton";
            this.temperatureSensorButton.Size = new System.Drawing.Size(124, 23);
            this.temperatureSensorButton.TabIndex = 3;
            this.temperatureSensorButton.Text = "Temperature";
            this.temperatureSensorButton.UseVisualStyleBackColor = false;
            this.temperatureSensorButton.Click += new System.EventHandler(this.temperatureSensorButton_Click);
            // 
            // bottomMotorButton
            // 
            this.bottomMotorButton.BackColor = System.Drawing.Color.Green;
            this.bottomMotorButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bottomMotorButton.Location = new System.Drawing.Point(64, 61);
            this.bottomMotorButton.Name = "bottomMotorButton";
            this.bottomMotorButton.Size = new System.Drawing.Size(124, 23);
            this.bottomMotorButton.TabIndex = 2;
            this.bottomMotorButton.Text = "Bottom Motor";
            this.bottomMotorButton.UseVisualStyleBackColor = false;
            this.bottomMotorButton.Click += new System.EventHandler(this.bottomMotorButton_Click);
            // 
            // topMotorButton
            // 
            this.topMotorButton.BackColor = System.Drawing.Color.Green;
            this.topMotorButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.topMotorButton.Location = new System.Drawing.Point(64, 32);
            this.topMotorButton.Name = "topMotorButton";
            this.topMotorButton.Size = new System.Drawing.Size(124, 23);
            this.topMotorButton.TabIndex = 1;
            this.topMotorButton.Text = "Top Motor";
            this.topMotorButton.UseVisualStyleBackColor = false;
            this.topMotorButton.Click += new System.EventHandler(this.topMotorButton_Click);
            // 
            // connectionsPanelLabel
            // 
            this.connectionsPanelLabel.AutoSize = true;
            this.connectionsPanelLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.connectionsPanelLabel.Location = new System.Drawing.Point(90, 9);
            this.connectionsPanelLabel.Name = "connectionsPanelLabel";
            this.connectionsPanelLabel.Size = new System.Drawing.Size(77, 13);
            this.connectionsPanelLabel.TabIndex = 0;
            this.connectionsPanelLabel.Text = "Connections";
            // 
            // manualControlPanel
            // 
            this.manualControlPanel.BackColor = System.Drawing.Color.White;
            this.manualControlPanel.Controls.Add(this.throttleLabel);
            this.manualControlPanel.Controls.Add(this.manualControlTrackBar);
            this.manualControlPanel.Controls.Add(this.manualArmButton);
            this.manualControlPanel.Controls.Add(this.manualControlPanelLabel);
            this.manualControlPanel.Location = new System.Drawing.Point(12, 261);
            this.manualControlPanel.Name = "manualControlPanel";
            this.manualControlPanel.Size = new System.Drawing.Size(255, 188);
            this.manualControlPanel.TabIndex = 2;
            // 
            // throttleLabel
            // 
            this.throttleLabel.AutoSize = true;
            this.throttleLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.throttleLabel.Location = new System.Drawing.Point(101, 96);
            this.throttleLabel.Name = "throttleLabel";
            this.throttleLabel.Size = new System.Drawing.Size(52, 13);
            this.throttleLabel.TabIndex = 4;
            this.throttleLabel.Text = "1000 us";
            // 
            // manualControlTrackBar
            // 
            this.manualControlTrackBar.Location = new System.Drawing.Point(15, 121);
            this.manualControlTrackBar.Maximum = 20;
            this.manualControlTrackBar.Name = "manualControlTrackBar";
            this.manualControlTrackBar.Size = new System.Drawing.Size(220, 45);
            this.manualControlTrackBar.TabIndex = 3;
            this.manualControlTrackBar.Scroll += new System.EventHandler(this.manualControlTrackBar_Scroll);
            // 
            // manualArmButton
            // 
            this.manualArmButton.BackColor = System.Drawing.Color.Green;
            this.manualArmButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.manualArmButton.Location = new System.Drawing.Point(87, 39);
            this.manualArmButton.Name = "manualArmButton";
            this.manualArmButton.Size = new System.Drawing.Size(75, 23);
            this.manualArmButton.TabIndex = 2;
            this.manualArmButton.Text = "Arm";
            this.manualArmButton.UseVisualStyleBackColor = false;
            this.manualArmButton.Click += new System.EventHandler(this.manualArmButton_Click);
            // 
            // manualControlPanelLabel
            // 
            this.manualControlPanelLabel.AutoSize = true;
            this.manualControlPanelLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.manualControlPanelLabel.Location = new System.Drawing.Point(84, 14);
            this.manualControlPanelLabel.Name = "manualControlPanelLabel";
            this.manualControlPanelLabel.Size = new System.Drawing.Size(92, 13);
            this.manualControlPanelLabel.TabIndex = 0;
            this.manualControlPanelLabel.Text = "Manual Control";
            // 
            // autoTestStartButton
            // 
            this.autoTestStartButton.BackColor = System.Drawing.Color.Green;
            this.autoTestStartButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.autoTestStartButton.Location = new System.Drawing.Point(87, 65);
            this.autoTestStartButton.Name = "autoTestStartButton";
            this.autoTestStartButton.Size = new System.Drawing.Size(75, 23);
            this.autoTestStartButton.TabIndex = 1;
            this.autoTestStartButton.Text = "Start";
            this.autoTestStartButton.UseVisualStyleBackColor = false;
            this.autoTestStartButton.Click += new System.EventHandler(this.autoTestStartButton_Click);
            // 
            // autoTestPanel
            // 
            this.autoTestPanel.BackColor = System.Drawing.Color.White;
            this.autoTestPanel.Controls.Add(this.autoTestPanelLabel);
            this.autoTestPanel.Controls.Add(this.autoTestStartButton);
            this.autoTestPanel.Location = new System.Drawing.Point(12, 455);
            this.autoTestPanel.Name = "autoTestPanel";
            this.autoTestPanel.Size = new System.Drawing.Size(255, 108);
            this.autoTestPanel.TabIndex = 3;
            // 
            // autoTestPanelLabel
            // 
            this.autoTestPanelLabel.AutoSize = true;
            this.autoTestPanelLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.autoTestPanelLabel.Location = new System.Drawing.Point(90, 30);
            this.autoTestPanelLabel.Name = "autoTestPanelLabel";
            this.autoTestPanelLabel.Size = new System.Drawing.Size(68, 13);
            this.autoTestPanelLabel.TabIndex = 2;
            this.autoTestPanelLabel.Text = "Ramp Test";
            // 
            // serialPort
            // 
            this.serialPort.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort_DataReceived);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1126, 575);
            this.Controls.Add(this.autoTestPanel);
            this.Controls.Add(this.manualControlPanel);
            this.Controls.Add(this.connectionsPanel);
            this.Controls.Add(this.portPanel);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.portPanel.ResumeLayout(false);
            this.portPanel.PerformLayout();
            this.connectionsPanel.ResumeLayout(false);
            this.connectionsPanel.PerformLayout();
            this.manualControlPanel.ResumeLayout(false);
            this.manualControlPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.manualControlTrackBar)).EndInit();
            this.autoTestPanel.ResumeLayout(false);
            this.autoTestPanel.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Panel portPanel;
        private System.Windows.Forms.Label portPanelLabel;
        private System.Windows.Forms.Label portLabel;
        private System.Windows.Forms.Button connectButton;
        private System.Windows.Forms.ComboBox portComboBox;
        private System.Windows.Forms.Panel connectionsPanel;
        private System.Windows.Forms.Label connectionsPanelLabel;
        private System.Windows.Forms.Panel manualControlPanel;
        private System.Windows.Forms.Button autoTestStartButton;
        private System.Windows.Forms.Label manualControlPanelLabel;
        private System.Windows.Forms.Button bottomMotorButton;
        private System.Windows.Forms.Button topMotorButton;
        private System.Windows.Forms.Button temperatureSensorButton;
        private System.Windows.Forms.Button manualArmButton;
        private System.Windows.Forms.Panel autoTestPanel;
        private System.Windows.Forms.Label autoTestPanelLabel;
        private System.Windows.Forms.TrackBar manualControlTrackBar;
        private System.Windows.Forms.Label throttleLabel;
        private System.IO.Ports.SerialPort serialPort;
    }
}

