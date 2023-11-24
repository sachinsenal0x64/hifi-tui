import requests
import time


class LeastConnectionsLoadBalancer:
    def __init__(self, server_list):
        self.server_list = server_list

    def get_least_connections_server(self):
        if not self.server_list:
            return None

        # Find the server with the least active connections
        min_con = float("inf")
        min_ser = None

        for server in self.server_list:
            con = server["connections"]
            if con < min_con:
                min_con = con
                min_ser = server
                print(min_ser)
        return min_ser

    def route_request(self, url):
        least_connections_server = self.get_least_connections_server()
        if least_connections_server:
            server_url = f"https://{least_connections_server['name']}"
            # Replace with your server's URL
            try:
                response = requests.get(server_url)
                return response.status_code
            except requests.exceptions.RequestException as e:
                # Handle connection errors, e.g., mark the server as unavailable
                least_connections_server["connections"] -= 1
                print(
                    f"Error while connecting to {least_connections_server['name']}: {e}"
                )
                print(
                    f"Decreasing connections for {least_connections_server['name']} to {least_connections_server['connections']}"
                )
                return "Error"

            finally:
                least_connections_server["connections"] += 1
                print(
                    f"Increase connection for {least_connections_server['name']} : {least_connections_server['connections']} "
                )

        else:
            return "No servers available."


# Example usage
server_list = [
    {"name": "youtube.com", "connections": 5},
    {"name": "reddit.com", "connections": 2},
    {"name": "github.com", "connections": 4},
]

load_balancer = LeastConnectionsLoadBalancer(server_list)

n = 1
while True:
    # Simulate distributing HTTP requests
    for i in range(n):
        response = load_balancer.route_request(f"http_request{i+1}")
        print(f"Response from server: {response}")
        time.sleep(2)
