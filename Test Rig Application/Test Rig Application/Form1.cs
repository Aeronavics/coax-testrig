using System;
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
        bool temperature_enabled = true;
        bool armed = false;
        bool in_test = false;

        public Form1()
        {
            InitializeComponent();
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
                    connectButton.BackColor = Color.Red;
                    MessageBox.Show("Serial port connected");
                }
                else
                {
                    serialPort.Close();
                    serialPort.Dispose();
                    connected  = false;
                    connectButton.BackColor = Color.Green;
                    MessageBox.Show("Serial port disconnected");
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
                        serialPort.Write("a");
                        top_motor_enabled = false;
                        topMotorButton.BackColor = Color.Red;
                    }
                    else
                    {
                        serialPort.Write("A");
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
                        serialPort.Write("b");
                        bottom_motor_enabled = false;
                        bottomMotorButton.BackColor = Color.Red;
                    }
                    else
                    {
                        serialPort.Write("B");
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

        private void temperatureSensorButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (connected && !armed && !in_test)
                {
                    if (temperature_enabled)
                    {
                        serialPort.Write("c");
                        temperature_enabled = false;
                        temperatureSensorButton.BackColor = Color.Red;
                    }
                    else
                    {
                        serialPort.Write("C");
                        temperature_enabled = true;
                        temperatureSensorButton.BackColor = Color.Green;
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
                            serialPort.Write("D");
                            armed = true;
                            manualArmButton.Text = "Disarm";
                            manualArmButton.BackColor = Color.Red;
                        }
                        else
                        {
                            manualControlTrackBar.Value = 0;
                            serialPort.Write("d");
                            armed = false;
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

        private void manualControlTrackBar_Scroll(object sender, EventArgs e)
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
                                case 0 :
                                    serialPort.Write("1000");
                                    break;
                                case 1 :
                                    serialPort.Write("1050");
                                    break;
                                case 2 :
                                    serialPort.Write("1100");
                                    break;
                                case 3 :
                                    serialPort.Write("1150");
                                    break;
                                case 4 :
                                    serialPort.Write("1200");
                                    break;
                                case 5 :
                                    serialPort.Write("1250");
                                    break;
                                case 6 :
                                    serialPort.Write("1300");
                                    break;
                                case 7 :
                                    serialPort.Write("1350");
                                    break;
                                case 8 :
                                    serialPort.Write("1400");
                                    break;
                                case 9 :
                                    serialPort.Write("1450");
                                    break;
                                case 10 :
                                    serialPort.Write("1500");
                                    break;
                                case 11 :
                                    serialPort.Write("1550");
                                    break;
                                case 12 :
                                    serialPort.Write("1600");
                                    break;
                                case 13 :
                                    serialPort.Write("1650");
                                    break;
                                case 14 :
                                    serialPort.Write("1700");
                                    break;
                                case 15 :
                                    serialPort.Write("1750");
                                    break;
                                case 16 :
                                    serialPort.Write("1800");
                                    break;
                                case 17 :
                                    serialPort.Write("1850");
                                    break;
                                case 18 :
                                    serialPort.Write("1900");
                                    break;
                                case 19 :
                                    serialPort.Write("1950");
                                    break;
                                case 20 :
                                    serialPort.Write("2000");
                                    break;
                            }
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
                            //Send message
                            in_test = true;
                            autoTestStartButton.Text = "Stop";
                            autoTestStartButton.BackColor = Color.Red;
                        }
                        else
                        {
                            //Send message
                            in_test = false; //Aslo need to do this when message recieved from arduino
                            autoTestStartButton.Text = "Start";
                            autoTestStartButton.BackColor = Color.Green;
                        }
                    }
                    else
                    {
                        MessageBox.Show("Disarm manual control before starting test");
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

        private void portComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void serialPort_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {

        }
    }
}