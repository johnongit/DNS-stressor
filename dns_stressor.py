import argparse
import dns.resolver
import time
import threading
import logging
from scapy.all import IP, UDP, DNS, DNSQR, send

def send_dns_query(server, record, num_queries, query_count, source_ip):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [server]

    for _ in range(num_queries):
        try:
            query = IP(src=source_ip, dst=server) / UDP(sport=12345, dport=53) / DNS(rd=1, qd=DNSQR(qname=record))
            send(query, verbose=False)
            query_count.append(1)
        except Exception:
            pass

def dns_load_generator(server, qps, record, duration, source_ip):
    num_queries = qps // threads
    extra_queries = qps % threads

    for i in range(duration):
        start_time = time.time()
        query_count = []

        thread_list = []
        for _ in range(threads):
            t = threading.Thread(target=send_dns_query, args=(server, record, num_queries, query_count, source_ip))
            thread_list.append(t)
            t.start()

        if extra_queries > 0:
            send_dns_query(server, record, extra_queries, query_count, source_ip)

        for t in thread_list:
            t.join()

        elapsed_time = time.time() - start_time
        actual_qps = len(query_count)
        logging.info(f"Second {i+1}: Sent {actual_qps} queries")

        if elapsed_time < 1:
            time.sleep(1 - elapsed_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS Load Generator")
    parser.add_argument("server", help="IP address of the DNS server")
    parser.add_argument("qps", type=int, help="Queries per second")
    parser.add_argument("record", help="DNS record to resolve")
    parser.add_argument("duration", type=int, help="Duration of the load generation in seconds")
    parser.add_argument("source_ip", help="Source IP address for the DNS queries")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    threads = 10  # Nombre de threads à utiliser

    dns_load_generator(args.server, args.qps, args.record, args.duration, args.source_ip)
