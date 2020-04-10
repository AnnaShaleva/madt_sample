from madt_lib.network import Network


def main():
    net = Network('15.0.0.0/8')

    # create network nodes
    node1 = net.create_node('node1', image='env_neo_go_one_image',
                            ports={'20333/tcp': 20333, '30333/tcp': 30333, '20001/tcp': 20001})
    node2 = net.create_node('node2', image='env_neo_go_two_image',
                            ports={'20334/tcp': 20334, '30334/tcp': 30334, '20002/tcp': 20002})
    node3 = net.create_node('node3', image='env_neo_go_three_image',
                            ports={'20335/tcp': 20335, '30335/tcp': 30335, '20003/tcp': 20003})
    node4 = net.create_node('node4', image='env_neo_go_four_image',
                            ports={'20336/tcp': 20336, '30336/tcp': 30336, '20004/tcp': 20004})

    # create a local network that will connect all those nodes
    net.create_subnet('net', (node1, node2, node3, node4))

    # distribute IP addresses
    net.configure(verbose=True)

    # save lab
    net.render('../../labs/basic_tutorial', verbose=True)


if __name__ == "__main__":
    main()
