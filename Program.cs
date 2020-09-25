using System;
using System.IO;
using System.Net;
using System.Text;

namespace Eve
{
    class Program
    {
        static void Main(string[] args)
        {
            WebRequest req = WebRequest.Create("https://miapi.pandorabots.com/talk");
            string postData = "input=hi";

            byte[] send = Encoding.Default.GetBytes(postData);
            req.Method = "POST";
            req.ContentType = "application/x-www-form-urlencoded";
            req.ContentLength = send.Length;

            Stream sout = req.GetRequestStream();
            sout.Write(send, 0, send.Length);
            sout.Flush();
            sout.Close();

            WebResponse res = req.GetResponse();
            StreamReader sr = new StreamReader(res.GetResponseStream());
            string returnvalue = sr.ReadToEnd();

            Console.WriteLine("Hello World!");
        }
    }
}
