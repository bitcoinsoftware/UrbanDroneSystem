import argparse, DroneClient
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--host", type=str, help="server host ip address")
    parser.add_argument("-p", "--port", type=int, help="port number")
    parser.add_argument("--videoport", type=int, help="video port number")
    args = parser.parse_args()
    a = DroneClient.DroneClient(args.host, args.port, args.videoport)
    a.steering()
