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
            this.bottomMotorButton = new System.Windows.Forms.Button();
            this.topMotorButton = new System.Windows.Forms.Button();
            this.connectionsPanelLabel = new System.Windows.Forms.Label();
            this.manualControlPanel = new System.Windows.Forms.Panel();
            this.manualThrottleSendButton = new System.Windows.Forms.Button();
            this.throttleLabel = new System.Windows.Forms.Label();
            this.manualControlTrackBar = new System.Windows.Forms.TrackBar();
            this.manualArmButton = new System.Windows.Forms.Button();
            this.manualControlPanelLabel = new System.Windows.Forms.Label();
            this.autoTestStartButton = new System.Windows.Forms.Button();
            this.autoTestPanel = new System.Windows.Forms.Panel();
            this.autoTestPanelLabel = new System.Windows.Forms.Label();
            this.serialPort = new System.IO.Ports.SerialPort(this.components);
            this.dataGridView = new System.Windows.Forms.DataGridView();
            this.downloadButton = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.clearDataButton = new System.Windows.Forms.Button();
            this.saveFileDialog = new System.Windows.Forms.SaveFileDialog();
            this.throttleValueLabel = new System.Windows.Forms.Label();
            this.panel2 = new System.Windows.Forms.Panel();
            this.panel5 = new System.Windows.Forms.Panel();
            this.thrustValueLabel = new System.Windows.Forms.Label();
            this.panel4 = new System.Windows.Forms.Panel();
            this.bottomMotorTemperatureValueLabel = new System.Windows.Forms.Label();
            this.bottomMotorCurrentValueLabel = new System.Windows.Forms.Label();
            this.bottomMotorVoltageValueLabel = new System.Windows.Forms.Label();
            this.bottomMotorPanelLabel = new System.Windows.Forms.Label();
            this.panel3 = new System.Windows.Forms.Panel();
            this.topMotorTemperatureValueLabel = new System.Windows.Forms.Label();
            this.topMotorCurrentValueLabel = new System.Windows.Forms.Label();
            this.topMotorPanelLabel = new System.Windows.Forms.Label();
            this.topMotorVoltageValueLabel = new System.Windows.Forms.Label();
            this.portPanel.SuspendLayout();
            this.connectionsPanel.SuspendLayout();
            this.manualControlPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.manualControlTrackBar)).BeginInit();
            this.autoTestPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView)).BeginInit();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel5.SuspendLayout();
            this.panel4.SuspendLayout();
            this.panel3.SuspendLayout();
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
            this.portComboBox.Click += new System.EventHandler(this.portComboBox_Click);
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
            this.connectButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.connectButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.connectButton.Location = new System.Drawing.Point(54, 78);
            this.connectButton.Name = "connectButton";
            this.connectButton.Size = new System.Drawing.Size(146, 23);
            this.connectButton.TabIndex = 5;
            this.connectButton.Text = "Connect";
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
            this.connectionsPanel.Controls.Add(this.bottomMotorButton);
            this.connectionsPanel.Controls.Add(this.topMotorButton);
            this.connectionsPanel.Controls.Add(this.connectionsPanelLabel);
            this.connectionsPanel.Location = new System.Drawing.Point(12, 132);
            this.connectionsPanel.Name = "connectionsPanel";
            this.connectionsPanel.Size = new System.Drawing.Size(255, 123);
            this.connectionsPanel.TabIndex = 1;
            // 
            // bottomMotorButton
            // 
            this.bottomMotorButton.BackColor = System.Drawing.Color.Green;
            this.bottomMotorButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.bottomMotorButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bottomMotorButton.Location = new System.Drawing.Point(64, 82);
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
            this.topMotorButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.topMotorButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.topMotorButton.Location = new System.Drawing.Point(64, 41);
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
            this.manualControlPanel.Controls.Add(this.manualThrottleSendButton);
            this.manualControlPanel.Controls.Add(this.throttleLabel);
            this.manualControlPanel.Controls.Add(this.manualControlTrackBar);
            this.manualControlPanel.Controls.Add(this.manualArmButton);
            this.manualControlPanel.Controls.Add(this.manualControlPanelLabel);
            this.manualControlPanel.Location = new System.Drawing.Point(12, 261);
            this.manualControlPanel.Name = "manualControlPanel";
            this.manualControlPanel.Size = new System.Drawing.Size(255, 188);
            this.manualControlPanel.TabIndex = 2;
            // 
            // manualThrottleSendButton
            // 
            this.manualThrottleSendButton.BackColor = System.Drawing.Color.Green;
            this.manualThrottleSendButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.manualThrottleSendButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.manualThrottleSendButton.Location = new System.Drawing.Point(87, 142);
            this.manualThrottleSendButton.Name = "manualThrottleSendButton";
            this.manualThrottleSendButton.Size = new System.Drawing.Size(75, 23);
            this.manualThrottleSendButton.TabIndex = 5;
            this.manualThrottleSendButton.Text = "Send";
            this.manualThrottleSendButton.UseVisualStyleBackColor = false;
            this.manualThrottleSendButton.Click += new System.EventHandler(this.manualThrottleSendButton_Click);
            // 
            // throttleLabel
            // 
            this.throttleLabel.AutoSize = true;
            this.throttleLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.throttleLabel.Location = new System.Drawing.Point(101, 75);
            this.throttleLabel.Name = "throttleLabel";
            this.throttleLabel.Size = new System.Drawing.Size(52, 13);
            this.throttleLabel.TabIndex = 4;
            this.throttleLabel.Text = "1000 us";
            // 
            // manualControlTrackBar
            // 
            this.manualControlTrackBar.Location = new System.Drawing.Point(14, 91);
            this.manualControlTrackBar.Maximum = 20;
            this.manualControlTrackBar.Name = "manualControlTrackBar";
            this.manualControlTrackBar.Size = new System.Drawing.Size(220, 45);
            this.manualControlTrackBar.TabIndex = 3;
            this.manualControlTrackBar.ValueChanged += new System.EventHandler(this.manualControlTrackBar_ValueChanged);
            // 
            // manualArmButton
            // 
            this.manualArmButton.BackColor = System.Drawing.Color.Green;
            this.manualArmButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
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
            this.autoTestStartButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.autoTestStartButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.autoTestStartButton.Location = new System.Drawing.Point(87, 53);
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
            this.autoTestPanelLabel.Location = new System.Drawing.Point(90, 18);
            this.autoTestPanelLabel.Name = "autoTestPanelLabel";
            this.autoTestPanelLabel.Size = new System.Drawing.Size(68, 13);
            this.autoTestPanelLabel.TabIndex = 2;
            this.autoTestPanelLabel.Text = "Ramp Test";
            // 
            // serialPort
            // 
            this.serialPort.BaudRate = 115200;
            this.serialPort.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort_DataReceived);
            // 
            // dataGridView
            // 
            this.dataGridView.AllowUserToAddRows = false;
            this.dataGridView.AllowUserToResizeColumns = false;
            this.dataGridView.AllowUserToResizeRows = false;
            this.dataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView.Location = new System.Drawing.Point(3, 3);
            this.dataGridView.Name = "dataGridView";
            this.dataGridView.ReadOnly = true;
            this.dataGridView.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.dataGridView.Size = new System.Drawing.Size(835, 396);
            this.dataGridView.TabIndex = 5;
            // 
            // downloadButton
            // 
            this.downloadButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.downloadButton.Location = new System.Drawing.Point(730, 405);
            this.downloadButton.Name = "downloadButton";
            this.downloadButton.Size = new System.Drawing.Size(108, 23);
            this.downloadButton.TabIndex = 6;
            this.downloadButton.Text = "Download CSV";
            this.downloadButton.UseVisualStyleBackColor = true;
            this.downloadButton.Click += new System.EventHandler(this.downloadButton_Click);
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.White;
            this.panel1.Controls.Add(this.clearDataButton);
            this.panel1.Controls.Add(this.dataGridView);
            this.panel1.Controls.Add(this.downloadButton);
            this.panel1.Location = new System.Drawing.Point(273, 132);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(841, 431);
            this.panel1.TabIndex = 7;
            // 
            // clearDataButton
            // 
            this.clearDataButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.clearDataButton.Location = new System.Drawing.Point(3, 405);
            this.clearDataButton.Name = "clearDataButton";
            this.clearDataButton.Size = new System.Drawing.Size(86, 23);
            this.clearDataButton.TabIndex = 7;
            this.clearDataButton.Text = "Clear Data";
            this.clearDataButton.UseVisualStyleBackColor = true;
            this.clearDataButton.Click += new System.EventHandler(this.clearDataButton_Click);
            // 
            // throttleValueLabel
            // 
            this.throttleValueLabel.AutoSize = true;
            this.throttleValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.throttleValueLabel.Location = new System.Drawing.Point(32, 18);
            this.throttleValueLabel.Name = "throttleValueLabel";
            this.throttleValueLabel.Size = new System.Drawing.Size(83, 13);
            this.throttleValueLabel.TabIndex = 8;
            this.throttleValueLabel.Text = "Throttle: 0 us";
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.Color.White;
            this.panel2.Controls.Add(this.panel5);
            this.panel2.Controls.Add(this.panel4);
            this.panel2.Controls.Add(this.panel3);
            this.panel2.Location = new System.Drawing.Point(276, 13);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(835, 116);
            this.panel2.TabIndex = 8;
            // 
            // panel5
            // 
            this.panel5.BackColor = System.Drawing.Color.WhiteSmoke;
            this.panel5.Controls.Add(this.throttleValueLabel);
            this.panel5.Controls.Add(this.thrustValueLabel);
            this.panel5.Location = new System.Drawing.Point(13, 11);
            this.panel5.Name = "panel5";
            this.panel5.Size = new System.Drawing.Size(150, 90);
            this.panel5.TabIndex = 8;
            // 
            // thrustValueLabel
            // 
            this.thrustValueLabel.AutoSize = true;
            this.thrustValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.thrustValueLabel.Location = new System.Drawing.Point(39, 57);
            this.thrustValueLabel.Name = "thrustValueLabel";
            this.thrustValueLabel.Size = new System.Drawing.Size(76, 13);
            this.thrustValueLabel.TabIndex = 9;
            this.thrustValueLabel.Text = "Thrust: 0 kg";
            // 
            // panel4
            // 
            this.panel4.BackColor = System.Drawing.Color.WhiteSmoke;
            this.panel4.Controls.Add(this.bottomMotorTemperatureValueLabel);
            this.panel4.Controls.Add(this.bottomMotorCurrentValueLabel);
            this.panel4.Controls.Add(this.bottomMotorVoltageValueLabel);
            this.panel4.Controls.Add(this.bottomMotorPanelLabel);
            this.panel4.Location = new System.Drawing.Point(169, 59);
            this.panel4.Name = "panel4";
            this.panel4.Size = new System.Drawing.Size(654, 42);
            this.panel4.TabIndex = 11;
            // 
            // bottomMotorTemperatureValueLabel
            // 
            this.bottomMotorTemperatureValueLabel.AutoSize = true;
            this.bottomMotorTemperatureValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bottomMotorTemperatureValueLabel.Location = new System.Drawing.Point(495, 18);
            this.bottomMotorTemperatureValueLabel.Name = "bottomMotorTemperatureValueLabel";
            this.bottomMotorTemperatureValueLabel.Size = new System.Drawing.Size(105, 13);
            this.bottomMotorTemperatureValueLabel.TabIndex = 3;
            this.bottomMotorTemperatureValueLabel.Text = "Temperature: 0 C";
            // 
            // bottomMotorCurrentValueLabel
            // 
            this.bottomMotorCurrentValueLabel.AutoSize = true;
            this.bottomMotorCurrentValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bottomMotorCurrentValueLabel.Location = new System.Drawing.Point(349, 18);
            this.bottomMotorCurrentValueLabel.Name = "bottomMotorCurrentValueLabel";
            this.bottomMotorCurrentValueLabel.Size = new System.Drawing.Size(75, 13);
            this.bottomMotorCurrentValueLabel.TabIndex = 2;
            this.bottomMotorCurrentValueLabel.Text = "Current: 0 A";
            // 
            // bottomMotorVoltageValueLabel
            // 
            this.bottomMotorVoltageValueLabel.AutoSize = true;
            this.bottomMotorVoltageValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bottomMotorVoltageValueLabel.Location = new System.Drawing.Point(195, 18);
            this.bottomMotorVoltageValueLabel.Name = "bottomMotorVoltageValueLabel";
            this.bottomMotorVoltageValueLabel.Size = new System.Drawing.Size(77, 13);
            this.bottomMotorVoltageValueLabel.TabIndex = 1;
            this.bottomMotorVoltageValueLabel.Text = "Voltage: 0 V";
            // 
            // bottomMotorPanelLabel
            // 
            this.bottomMotorPanelLabel.AutoSize = true;
            this.bottomMotorPanelLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.bottomMotorPanelLabel.Location = new System.Drawing.Point(14, 18);
            this.bottomMotorPanelLabel.Name = "bottomMotorPanelLabel";
            this.bottomMotorPanelLabel.Size = new System.Drawing.Size(82, 13);
            this.bottomMotorPanelLabel.TabIndex = 0;
            this.bottomMotorPanelLabel.Text = "Bottom Motor";
            // 
            // panel3
            // 
            this.panel3.BackColor = System.Drawing.Color.WhiteSmoke;
            this.panel3.Controls.Add(this.topMotorTemperatureValueLabel);
            this.panel3.Controls.Add(this.topMotorCurrentValueLabel);
            this.panel3.Controls.Add(this.topMotorPanelLabel);
            this.panel3.Controls.Add(this.topMotorVoltageValueLabel);
            this.panel3.Location = new System.Drawing.Point(169, 11);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(654, 42);
            this.panel3.TabIndex = 10;
            // 
            // topMotorTemperatureValueLabel
            // 
            this.topMotorTemperatureValueLabel.AutoSize = true;
            this.topMotorTemperatureValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.topMotorTemperatureValueLabel.Location = new System.Drawing.Point(495, 16);
            this.topMotorTemperatureValueLabel.Name = "topMotorTemperatureValueLabel";
            this.topMotorTemperatureValueLabel.Size = new System.Drawing.Size(105, 13);
            this.topMotorTemperatureValueLabel.TabIndex = 13;
            this.topMotorTemperatureValueLabel.Text = "Temperature: 0 C";
            // 
            // topMotorCurrentValueLabel
            // 
            this.topMotorCurrentValueLabel.AutoSize = true;
            this.topMotorCurrentValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.topMotorCurrentValueLabel.Location = new System.Drawing.Point(349, 16);
            this.topMotorCurrentValueLabel.Name = "topMotorCurrentValueLabel";
            this.topMotorCurrentValueLabel.Size = new System.Drawing.Size(75, 13);
            this.topMotorCurrentValueLabel.TabIndex = 12;
            this.topMotorCurrentValueLabel.Text = "Current: 0 A";
            // 
            // topMotorPanelLabel
            // 
            this.topMotorPanelLabel.AutoSize = true;
            this.topMotorPanelLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.topMotorPanelLabel.Location = new System.Drawing.Point(14, 18);
            this.topMotorPanelLabel.Name = "topMotorPanelLabel";
            this.topMotorPanelLabel.Size = new System.Drawing.Size(65, 13);
            this.topMotorPanelLabel.TabIndex = 11;
            this.topMotorPanelLabel.Text = "Top Motor";
            // 
            // topMotorVoltageValueLabel
            // 
            this.topMotorVoltageValueLabel.AutoSize = true;
            this.topMotorVoltageValueLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.topMotorVoltageValueLabel.Location = new System.Drawing.Point(195, 16);
            this.topMotorVoltageValueLabel.Name = "topMotorVoltageValueLabel";
            this.topMotorVoltageValueLabel.Size = new System.Drawing.Size(77, 13);
            this.topMotorVoltageValueLabel.TabIndex = 10;
            this.topMotorVoltageValueLabel.Text = "Voltage: 0 V";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1126, 575);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.autoTestPanel);
            this.Controls.Add(this.manualControlPanel);
            this.Controls.Add(this.connectionsPanel);
            this.Controls.Add(this.portPanel);
            this.Name = "Form1";
            this.Text = "Form1";
            this.portPanel.ResumeLayout(false);
            this.portPanel.PerformLayout();
            this.connectionsPanel.ResumeLayout(false);
            this.connectionsPanel.PerformLayout();
            this.manualControlPanel.ResumeLayout(false);
            this.manualControlPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.manualControlTrackBar)).EndInit();
            this.autoTestPanel.ResumeLayout(false);
            this.autoTestPanel.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel2.ResumeLayout(false);
            this.panel5.ResumeLayout(false);
            this.panel5.PerformLayout();
            this.panel4.ResumeLayout(false);
            this.panel4.PerformLayout();
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
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
        private System.Windows.Forms.Button manualArmButton;
        private System.Windows.Forms.Panel autoTestPanel;
        private System.Windows.Forms.Label autoTestPanelLabel;
        private System.Windows.Forms.TrackBar manualControlTrackBar;
        private System.Windows.Forms.Label throttleLabel;
        private System.IO.Ports.SerialPort serialPort;
        private System.Windows.Forms.Button manualThrottleSendButton;
        private System.Windows.Forms.DataGridView dataGridView;
        private System.Windows.Forms.Button downloadButton;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog;
        private System.Windows.Forms.Button clearDataButton;
        private System.Windows.Forms.Label throttleValueLabel;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel5;
        private System.Windows.Forms.Label thrustValueLabel;
        private System.Windows.Forms.Panel panel4;
        private System.Windows.Forms.Label bottomMotorPanelLabel;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Label topMotorTemperatureValueLabel;
        private System.Windows.Forms.Label topMotorCurrentValueLabel;
        private System.Windows.Forms.Label topMotorPanelLabel;
        private System.Windows.Forms.Label topMotorVoltageValueLabel;
        private System.Windows.Forms.Label bottomMotorTemperatureValueLabel;
        private System.Windows.Forms.Label bottomMotorCurrentValueLabel;
        private System.Windows.Forms.Label bottomMotorVoltageValueLabel;
    }
}

