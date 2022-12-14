using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

// check whether all required namespaces are imported
namespace Client {
class Program {
public class SynchronousSocketClient
{
    public static int Main(String[] args)
    {
        StartClient();
        return 0;
    }
       

        public static void StartClient()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];

        // Connect to a remote device.  
        try
        {
            // Establish the remote endpoint for the socket.  
            // check if the port is defined or not
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = ipHostInfo.AddressList[0];
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 11000);

            // Check whether TCP Socket is created correctly
            Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            // Connect the socket to the remote endpoint. Catch any errors.  
            try
            {
                sender.Connect(remoteEP);

                Console.WriteLine("Socket connected to -> {0} ",
                          sender.RemoteEndPoint.ToString());

                // check if the variable is defined correctly or not
                string name;
                string intrests;
                string mail;
                Console.WriteLine("Enter the Person Name: ");
                name = Console.ReadLine();
                Console.WriteLine("Enter the Person Interest: ");
                intrests = Console.ReadLine();
                Console.WriteLine("Enter the Person Email: ");
                mail = Console.ReadLine();
                // Encode the data string into a byte array.  
                // check the data type of the data you are sending.
                byte[] msg = Encoding.ASCII.GetBytes(name + "," + intrests + "," + mail);

                // Send the data through the socket.  
                int byteSent = sender.Send(msg);

                // Close the socket.
               byte[] messageReceived = new byte[1024];
                sender.Shutdown(SocketShutdown.Both);
            sender.Close();
            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }

        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
    }

    // check the main function
    

    private static void Start()
    {
        throw new NotImplementedException();
    }
}
}
}