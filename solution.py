from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1',  msg = "\r\n My message", \
        subject = None, emailFrom = 'alice@crepes.fr', emailTo = 'bob@hamburgers.edu'):
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end


    recv = clientSocket.recv(1024).decode()
    #print(recv)


    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)


    # Send MAIL FROM command and print server response.
    mailFrom = 'MAIL FROM: <{}>\r\n'.format(emailFrom)
    clientSocket.send(mailFrom.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)


    # Send RCPT TO command and print server response.
    recipientTo = 'RCPT TO: <{}>\r\n'.format(emailTo)
    clientSocket.send(recipientTo.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)


    # Send DATA command and print server response.
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)



    # Send message data.
    if(subject is not None):
        msg = 'Subject: {}\r\n{}'.format(subject, msg)
    msg = 'From: {}\r\nTo: {}\r\n{}'.format(emailFrom, emailTo, msg)
    clientSocket.send(msg.encode())


    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)


    # Send QUIT command and get server response.
    recipientTo = 'QUIT\r\n'
    clientSocket.send(recipientTo.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv)
    clientSocket.close()


if __name__ == '__main__':

    #subject = 'Did you ever hear the tragedy of Darth Plagueis The Wise?'
    #message = (' I thought not. It’s not a story the Jedi would tell you.\r\n\r\n'
    #            'It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… '
    #            'He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. '
    #            'The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did.\r\n\r\n'
    #            'Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic.\r\n\r\nHe could save others from death, but not himself.')
    smtp_client()
