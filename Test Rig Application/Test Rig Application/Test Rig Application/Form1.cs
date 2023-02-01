using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Test_Rig_Application
{
    public partial class Form1 : Form
    {
        bool connected = false;
        bool top_motor_enabled = true;
        bool bottom_motor_enabled = true;
        bool armed = false;
        bool in_test = false;

        DataTable data = new DataTable();

        public Form1()
        {
            InitializeComponent();
            portComboBox.DataSource = SerialPort.GetPortNames();
            BindDataGridView();
        }



        private void portComboBox_Click(object sender, EventArgs e)
        {
            portComboBox.DataSource = SerialPort.GetPortNames();
        }

        private void connectButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (!connected)
                {
                    serialPort.PortName = portComboBox.SelectedItem.ToString();
                    serialPort.Open();
                    connected = true;
                    connectButton.Text = "Disconnect";
                    connectButton.BackColor = Color.Red;
                }
                else
                {
                    serialPort.Write("DARM");
                    armed = false;
                    manualControlTrackBar.Value = 0;
                    manualArmButton.Text = "Arm";
                    manualArmButton.BackColor = Color.Green;

                    in_test = false;
                    autoTestStartButton.Text = "Start";
                    autoTestStartButton.BackColor = Color.Green;

                    serialPort.Close();
                    serialPort.Dispose();
                    connected  = false;
                    connectButton.Text = "Connect";
                    connectButton.BackColor = Color.Green;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }



        private void topMotorButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (connected && !armed && !in_test)
                {
                    if (top_motor_enabled)
                    {
                        top_motor_enabled = false;
                        topMotorButton.BackColor = Color.Red;
                    }
                    else
                    {
                        top_motor_enabled = true;
                        topMotorButton.BackColor = Color.Green;
                    }
                }
                else
                {
                    MessageBox.Show("Connect to a COM port");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void bottomMotorButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (connected && !armed && !in_test)
                {
                    if (bottom_motor_enabled)
                    {
                        bottom_motor_enabled = false;
                        bottomMotorButton.BackColor = Color.Red;
                    }
                    else
                    {
                        bottom_motor_enabled = true;
                        bottomMotorButton.BackColor = Color.Green;
                    }
                }
                else
                {
                    MessageBox.Show("Connect to a COM port");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }



        private void manualArmButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (connected)
                {
                    if (!in_test)
                    {
                        if (!armed)
                        {
                            String command_out = "MARM,";
                            if (top_motor_enabled)
                            {
                                command_out += "M1ON,";
                            }
                            else
                            {
                                command_out += "M1OF,";
                            }
                            if (bottom_motor_enabled)
                            {
                                command_out += "M2ON";
                            }
                            else
                            {
                                command_out += "M2OF";
                            }
                            serialPort.Write(command_out);
                            armed = true;
                            manualArmButton.Text = "Disarm";
                            manualArmButton.BackColor = Color.Red;
                        }
                        else
                        {
                            serialPort.Write("DARM");
                            armed = false;
                            manualControlTrackBar.Value = 0;
                            manualArmButton.Text = "Arm";
                            manualArmButton.BackColor = Color.Green;
                        }
                    }
                    else
                    {
                        MessageBox.Show("Test in progress");
                    }
                }
                else
                {
                    MessageBox.Show("Connect to a COM port");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void manualControlTrackBar_ValueChanged(object sender, EventArgs e)
        {
            if (connected)
            {
                if (!in_test)
                {
                    if (armed)
                    {
                        throttleLabel.Text = (manualControlTrackBar.Value * 50 + 1000).ToString() + " us";
                    }
                    else
                    {
                        manualControlTrackBar.Value = 0;
                        MessageBox.Show("Arm motors before increasing throttle");
                    }
                }
                else
                {
                    manualControlTrackBar.Value = 0;
                    MessageBox.Show("Test in progress");
                }
            }
            else
            {
                manualControlTrackBar.Value = 0;
                MessageBox.Show("Connect to a COM port");
            }
        }

        private void manualThrottleSendButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (connected)
                {
                    if (!in_test)
                    {
                        if (armed)
                        {
                            switch (manualControlTrackBar.Value)
                            {
                                case 0:
                                    serialPort.Write("1000");
                                    break;
                                case 1:
                                    serialPort.Write("1050");
                                    break;
                                case 2:
                                    serialPort.Write("1100");
                                    break;
                                case 3:
                                    serialPort.Write("1150");
                                    break;
                                case 4:
                                    serialPort.Write("1200");
                                    break;
                                case 5:
                                    serialPort.Write("1250");
                                    break;
                                case 6:
                                    serialPort.Write("1300");
                                    break;
                                case 7:
                                    serialPort.Write("1350");
                                    break;
                                case 8:
                                    serialPort.Write("1400");
                                    break;
                                case 9:
                                    serialPort.Write("1450");
                                    break;
                                case 10:
                                    serialPort.Write("1500");
                                    break;
                                case 11:
                                    serialPort.Write("1550");
                                    break;
                                case 12:
                                    serialPort.Write("1600");
                                    break;
                                case 13:
                                    serialPort.Write("1650");
                                    break;
                                case 14:
                                    serialPort.Write("1700");
                                    break;
                                case 15:
                                    serialPort.Write("1750");
                                    break;
                                case 16:
                                    serialPort.Write("1800");
                                    break;
                                case 17:
                                    serialPort.Write("1850");
                                    break;
                                case 18:
                                    serialPort.Write("1900");
                                    break;
                                case 19:
                                    serialPort.Write("1950");
                                    break;
                                case 20:
                                    serialPort.Write("2000");
                                    break;
                            }
                        }
                        else
                        {
                            MessageBox.Show("Arm motors before increasing throttle");
                        }
                    }
                    else
                    {
                        MessageBox.Show("Test in progress");
                    }
                }
                else
                {
                    MessageBox.Show("Connect to a COM port");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void autoTestStartButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (connected)
                {
                    if (!armed)
                    {
                        if (!in_test)
                        {
                            String command_out = "STAR,";
                            if (top_motor_enabled)
                            {
                                command_out += "M1ON,";
                            }
                            else
                            {
                                command_out += "M1OF,";
                            }
                            if (bottom_motor_enabled)
                            {
                                command_out += "M2ON";
                            }
                            else
                            {
                                command_out += "M2OF";
                            }
                            serialPort.Write(command_out);
                            in_test = true;
                            autoTestStartButton.Text = "Stop";
                            autoTestStartButton.BackColor = Color.Red;
                        }
                        else
                        {
                            serialPort.Write("DARM");
                            in_test = false;
                            autoTestStartButton.Text = "Start";
                            autoTestStartButton.BackColor = Color.Green;
                        }
                    }
                    else
                    {
                        MessageBox.Show("Disarm motors before starting test");
                    }
                }
                else
                {
                    MessageBox.Show("Connect to a COM port");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }



        private void serialPort_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            try
            {
                string[] in_data = serialPort.ReadLine().Split(',');

                int throttle = int.Parse(in_data[0]);
                float thrust = float.Parse(in_data[1]),
                    top_motor_voltage = float.Parse(in_data[2]),
                    top_motor_current = float.Parse(in_data[3]),
                    bottom_motor_voltage = float.Parse(in_data[4]),
                    bottom_motor_current = float.Parse(in_data[5]),
                    top_motor_temperature = float.Parse(in_data[6]),
                    bottom_motor_temperature = float.Parse(in_data[7]);

                if (top_motor_temperature < 0)
                {
                    top_motor_temperature = 0;
                }
                if (bottom_motor_temperature < 0)
                {
                    bottom_motor_temperature = 0;
                }

                //throttleValueLabel.Text = "Throttle: " + throttle.ToString() + " us";
                //thrustValueLabel.Text = "Thrust: " + thrust.ToString() + " kg";
                //topMotorVoltageValueLabel.Text = "Voltage: " + top_motor_voltage.ToString() + " V";
                //topMotorCurrentValueLabel.Text = "Current: " + top_motor_current.ToString() + " A";
                //bottomMotorVoltageValueLabel.Text = "Voltage: " + bottom_motor_voltage.ToString() + " V";
                //bottomMotorCurrentValueLabel.Text = "Current: " + bottom_motor_current.ToString() + " A";
                //topMotorTemperatureValueLabel.Text = "Temperature: " + top_motor_temperature.ToString() + " C";
                //bottomMotorTemperatureValueLabel.Text = "Temperature " + bottom_motor_temperature.ToString() + " C";

                if (in_test)
                {
                    data.Rows.Add(throttle, thrust, top_motor_voltage, top_motor_current, bottom_motor_voltage, bottom_motor_current,
                        top_motor_temperature, bottom_motor_temperature);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }



        private void BindDataGridView()
        {
            data.Columns.AddRange(new DataColumn[8]
            {
                new DataColumn("Throttle (us)", typeof(int)),
                new DataColumn("Thrust (kg)", typeof(float)),
                new DataColumn("Top Motor Voltage (V)", typeof(float)),
                new DataColumn("Top Motor Current (A)", typeof(float)),
                new DataColumn("Bottom Motor Voltage (V)", typeof(float)),
                new DataColumn("Bottom Motor Current (A)", typeof(float)),
                new DataColumn("Top Motor Temperature (C)", typeof(float)),
                new DataColumn("Bottom Motor Temperature (C)", typeof(float))
            });
            dataGridView.DataSource = data;
        }

        private void clearDataButton_Click(object sender, EventArgs e)
        {
            try
            {
                data.Clear();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void downloadButton_Click(object sender, EventArgs e)
        {
            try
            {
                string csv = string.Empty;

                foreach (DataGridViewColumn column in dataGridView.Columns)
                {
                    csv += column.HeaderText + ',';
                }

                csv += "\r\n";

                foreach (DataGridViewRow row in dataGridView.Rows)
                {
                    foreach (DataGridViewCell cell in row.Cells)
                    {
                        csv += cell.Value.ToString().Replace(",", ";") + ',';
                    }

                    csv += "\r\n";
                }

                saveFileDialog.Filter = "CSV files|*.csv";

                using (saveFileDialog)
                {
                    if (saveFileDialog.ShowDialog() == DialogResult.OK)
                    {
                        File.WriteAllText(saveFileDialog.FileName, csv);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}