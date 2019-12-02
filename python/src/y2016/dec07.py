import re

re_HYPERNET = re.compile(r"(\[\w+\])")
re_ABBA = re.compile(r"(\w)((?!\1)\w)\2\1")
re_ABA = re.compile(r"(?=((\w)((?!\2)\w)\2))")


def split_ip_hypernets(ip):
    hyper, not_hyper = [], []
    start = 0
    for match in re_HYPERNET.finditer(ip):
        match_start = match.start()
        match_end = match.end()
        if match_start > start:
            not_hyper.append(ip[start:match_start])
        start = match_end
        hyper.append(match.group(0))
    not_hyper.append(ip[start:])
    return hyper, not_hyper


def ipv7_supports_tls(ip):
    hyper, non_hyper = split_ip_hypernets(ip)
    if any(re_ABBA.search(x) for x in hyper):
        return False
    else:
        return any(re_ABBA.search(x) for x in non_hyper)


def ipv7_supports_ssl(ip):
    hyper, non_hyper = split_ip_hypernets(ip)
    hyper = "".join(hyper)
    non_hyper = "-".join(non_hyper)

    for match in re_ABA.finditer(non_hyper):
        ABA = match.group(1)
        BAB = ABA[1] + ABA[0] + ABA[1]
        if BAB in hyper:
            return True
    return False


def count_ips_with_tls(ips):
    return len(list(filter(ipv7_supports_tls, ips)))


def count_ips_with_ssl(ips):
    return len(list(filter(ipv7_supports_ssl, ips)))


if __name__ == '__main__':
    with open('../../../data/2016/input.7.txt', 'r') as fh:
        lines = fh.readlines()
        print("Number of IPs that support TLS", count_ips_with_tls(lines))
        print("Number of IPs that support SSL", count_ips_with_ssl(lines))
