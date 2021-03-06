#!/usr/bin/python

 # __    __                                                __       __                       __      __                                   
# |  \  |  \                                              |  \     /  \                     |  \    |  \                                  
# | $$  | $$  ______   _______    ______   __    __       | $$\   /  $$  ______    ______  _| $$_    \$$ ______ ____    ______    ______  
# | $$__| $$ /      \ |       \  /      \ |  \  |  \      | $$$\ /  $$$ /      \  /      \|   $$ \  |  \|      \    \  /      \  /      \ 
# | $$    $$|  $$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$      | $$$$\  $$$$|  $$$$$$\|  $$$$$$\\$$$$$$  | $$| $$$$$$\$$$$\|  $$$$$$\|  $$$$$$\
# | $$$$$$$$| $$    $$| $$  | $$| $$   \$$| $$  | $$      | $$\$$ $$ $$| $$  | $$| $$   \$$ | $$ __ | $$| $$ | $$ | $$| $$    $$| $$   \$$
# | $$  | $$| $$$$$$$$| $$  | $$| $$      | $$__/ $$      | $$ \$$$| $$| $$__/ $$| $$       | $$|  \| $$| $$ | $$ | $$| $$$$$$$$| $$      
# | $$  | $$ \$$     \| $$  | $$| $$       \$$    $$      | $$  \$ | $$ \$$    $$| $$        \$$  $$| $$| $$ | $$ | $$ \$$     \| $$      
 # \$$   \$$  \$$$$$$$ \$$   \$$ \$$       _\$$$$$$$       \$$      \$$  \$$$$$$  \$$         \$$$$  \$$ \$$  \$$  \$$  \$$$$$$$ \$$      
 #                                        |  \__| $$                                                                                      
 #                                         \$$    $$                                                                                      
 #                                          \$$$$$$                                                                                       
 #  ______    ______   __       __  _______    ______    ______    ______   _______                                                       
 # /      \  /      \ |  \     /  \|       \  /      \  /      \  /      \ |       \                                                      
# |  $$$$$$\|  $$$$$$\| $$\   /  $$| $$$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$                                                      
# | $$   \$$| $$  | $$| $$$\ /  $$$| $$__/ $$ \$$__| $$| $$$\| $$ \$$__| $$| $$____                                                       
# | $$      | $$  | $$| $$$$\  $$$$| $$    $$  |     $$| $$$$\ $$  |     $$| $$    \                                                      
# | $$   __ | $$  | $$| $$\$$ $$ $$| $$$$$$$  __\$$$$$\| $$\$$\$$ __\$$$$$\ \$$$$$$$\                                                     
# | $$__/  \| $$__/ $$| $$ \$$$| $$| $$      |  \__| $$| $$_\$$$$|  \__| $$|  \__| $$                                                     
 # \$$    $$ \$$    $$| $$  \$ | $$| $$       \$$    $$ \$$  \$$$ \$$    $$ \$$    $$                                                     
 #  \$$$$$$   \$$$$$$  \$$      \$$ \$$        \$$$$$$   \$$$$$$   \$$$$$$   \$$$$$$                                                      
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
 # _______   __    __   ______         _______                                 __                                                         
# |       \ |  \  |  \ /      \       |       \                               |  \                                                        
# | $$$$$$$\| $$\ | $$|  $$$$$$\      | $$$$$$$\  ______    _______   ______  | $$ __     __   ______    ______                           
# | $$  | $$| $$$\| $$| $$___\$$      | $$__| $$ /      \  /       \ /      \ | $$|  \   /  \ /      \  /      \                          
# | $$  | $$| $$$$\ $$ \$$    \       | $$    $$|  $$$$$$\|  $$$$$$$|  $$$$$$\| $$ \$$\ /  $$|  $$$$$$\|  $$$$$$\                         
# | $$  | $$| $$\$$ $$ _\$$$$$$\      | $$$$$$$\| $$    $$ \$$    \ | $$  | $$| $$  \$$\  $$ | $$    $$| $$   \$$                         
# | $$__/ $$| $$ \$$$$|  \__| $$      | $$  | $$| $$$$$$$$ _\$$$$$$\| $$__/ $$| $$   \$$ $$  | $$$$$$$$| $$                               
# | $$    $$| $$  \$$$ \$$    $$      | $$  | $$ \$$     \|       $$ \$$    $$| $$    \$$$    \$$     \| $$                               
 # \$$$$$$$  \$$   \$$  \$$$$$$        \$$   \$$  \$$$$$$$ \$$$$$$$   \$$$$$$  \$$     \$      \$$$$$$$ \$$                               

from copy import copy
from optparse import OptionParser, OptionValueError
import pprint
from random import seed, randint
import struct
from socket import *
from sys import exit, maxint as MAXINT
from time import time, sleep

from gz01.collections_backport import OrderedDict
from gz01.dnslib.RR import *
from gz01.dnslib.Header import Header
from gz01.dnslib.QE import QE
from gz01.inetlib.types import *
from gz01.util import *

# timeout in seconds to wait for reply
TIMEOUT = 5

# domain name and internet address of a root name server
ROOTNS_DN = "a.root-servers.net."
ROOTNS_IN_ADDR = "198.41.0.4"


class ACacheEntry:
    ALPHA = 0.8

    def __init__(self, dict, srtt=None):
        self._srtt = srtt
        self._dict = dict

        def __repr__(self):
            return "<ACE %s, srtt=%s>" % \
                (self._dict, ("*" if self._srtt is None else self._srtt))

        def update_rtt(self, rtt):
            old_srtt = self._srtt
            self._srtt = rtt if self._srtt is None else \
                (rtt*(1.0 - self.ALPHA) + self._srtt*self.ALPHA)
            logger.debug("update_rtt: rtt %f updates srtt %s --> %s" %
                         (rtt, ("*" if old_srtt is None else old_srtt), self._srtt,))


class CacheEntry:
    def __init__(self, expiration=MAXINT, authoritative=False):
        self._expiration = expiration
        self._authoritative = authoritative

    def __repr__(self):
        now = int(time())
        return "<CE exp=%ds auth=%s>" % \
            (self._expiration - now, self._authoritative,)


class CnameCacheEntry:
    def __init__(self, cname, expiration=MAXINT, authoritative=False):
        self._cname = cname
        self._expiration = expiration
        self._authoritative = authoritative

    def __repr__(self):
        now = int(time())
        return "<CCE cname=%s exp=%ds auth=%s>" % \
            (self._cname, self._expiration - now, self._authoritative,)


# >>> entry point of ncsdns.py <<<

# Seed random number generator with current time of day:
now = int(time())
seed(now)

# Initialize the pretty printer:
pp = pprint.PrettyPrinter(indent=3)

# Initialize the name server cache data structure;
# [domain name --> [nsdn --> CacheEntry]]:
nscache = dict([(DomainName("."),
                 OrderedDict([(DomainName(ROOTNS_DN),
                               CacheEntry(expiration=MAXINT,
                               authoritative=True))]))])

# Initialize the address cache data structure;
# [domain name --> [in_addr --> CacheEntry]]:
acache = dict([(DomainName(ROOTNS_DN),
                ACacheEntry(dict([(InetAddr(ROOTNS_IN_ADDR),
                                   CacheEntry(expiration=MAXINT,
                                   authoritative=True))])))])

# Initialize the cname cache data structure;
# [domain name --> CnameCacheEntry]
cnamecache = dict([])


# Parse the command line and assign us an ephemeral port to listen on:
def check_port(option, opt_str, value, parser):
    if value < 32768 or value > 61000:
        if value != 53:
            raise OptionValueError("need 32768 <= port <= 61000")
    parser.values.port = value

parser = OptionParser()
parser.add_option("-p", "--port", dest="port", type="int", action="callback",
                  callback=check_port, metavar="PORTNO", default=0,
                  help="UDP port to listen on (default: use an unused ephemeral port)")
(options, args) = parser.parse_args()

# Create a server socket to accept incoming connections from DNS
# client resolvers (stub resolvers):
ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(("127.0.0.1", options.port))
serveripaddr, serverport = ss.getsockname()

# NOTE: In order to pass the test suite, the following must be the
# first line that your dns server prints and flushes within one
# second, to sys.stdout:
print "%s: listening on port %d" % (sys.argv[0], serverport)
sys.stdout.flush()

# Create a client socket on which to send requests to other DNS
# servers:
setdefaulttimeout(TIMEOUT)
cs = socket(AF_INET, SOCK_DGRAM)

#--------------------------------------------------------------------------------------------------#
#                                             Parsing code                                         #
#--------------------------------------------------------------------------------------------------#

#Takes raw data, checks header has valid values and returns the query id and the list of QE objects
def parseRequest(data):
    requestHeader = Header.fromData(data)
    try:
        assert(requestHeader._opcode == Header.OPCODE_QUERY)
        assert(requestHeader._rcode == Header.RCODE_NOERR)
        assert(requestHeader._qr == False)
    except AssertionError:
        raise ValueError("Incorrectly formatted request")
    noOfQueries = requestHeader._qdcount
    offset = requestHeader.__len__()
    queries = []
    for i in range(noOfQueries):
        queries.append(QE.fromData(data, offset))
        offset += queries[i].__len__()
        if str(queries[i]) == "NIMPL":
            raise NotImplementedError 

    return (requestHeader._id, queries)
#Takes data and seperates it into list of resource records
def parseRecords(data, offset, noOfItems):
    values = []
    for i in range(noOfItems):
        (record, length) = RR.fromData(data, offset)
        values.append(record)
        offset += length #increase offset by length of compressed data
    return (offset, values)

def parseQuestions(data, offset, noOfQuestions):
    questions = []
    for i in range(noOfQuestions):
        questions.append(QE.fromData(data, offset))
        offset += len(questions[i])#increase offset by length of previous question
    return (offset, questions)

#gets header and resource records out of data then caches the results
def parseResponse(data, _id):
    responseHeader = Header.fromData(data)
    try: #check for valid header codes
        assert(responseHeader._id == _id)
        assert(responseHeader._opcode == Header.OPCODE_QUERY)
        assert(responseHeader._qr == True)
    except AssertionError:
        raise AttributeError
    try:
        assert(responseHeader._rcode == Header.RCODE_NOERR)
    except AssertionError:
        error = responseHeader._rcode
        if error == Header.RCODE_NAMEERR:
            raise NameError("Name not found")


    noOfQuestions = responseHeader._qdcount
    noOfAnswers = responseHeader._ancount
    noOfAuthorities = responseHeader._nscount
    noOfAdditional = responseHeader._arcount
    
    offset = len(responseHeader)
    
    (offset, questions) = parseQuestions(data, offset, noOfQuestions)
    (offset, answers) = parseRecords(data, offset, noOfAnswers)
    (offset, authorities) = parseRecords(data, offset, noOfAuthorities)
    (offset, additional) = parseRecords(data, offset, noOfAdditional)

    cacheAnswers(answers)
    cacheNameServers(authorities, additional)

    return (questions, answers, authorities, additional)

#---------------------------------------------------------------------------------------------------------#
#                                                 Caching code                                            #
#---------------------------------------------------------------------------------------------------------#

#checks if an a record is already in cache, if so replace it otherwise create new AcacheEntry and insert it
def insertToACache(aRecord):
    expiration = aRecord._ttl + int(time())
    domain = aRecord._dn
    address = InetAddr.fromNetwork(aRecord._addr)
    if domain in acache:
        acache[domain]._dict[address] = CacheEntry(expiration=expiration, authoritative=True)
    else:
        d = dict([(address,CacheEntry(expiration=expiration,authoritative=True))])
        acache[domain] = ACacheEntry(d)

#takes a list of answers and adds A records to a cache and c records to c cache
def cacheAnswers(answers):
    for answer in answers:
        if answer._type == RR.TYPE_A:
            insertToACache(answer)
        elif answer._type == RR.TYPE_CNAME:
            domain = answer._dn
            cname = answer._cname
            expiration = answer._ttl + int(time())
            cnamecache[domain] = CnameCacheEntry(cname, expiration)

#adds NS records to ns cache and additional records to a cache
def cacheNameServers(authorities, additional):
    for authority in authorities:
        if authority._type == RR.TYPE_NS:
            expiration = authority._ttl +int(time())
            domain = authority._dn
            nsDomain = authority._nsdn
            if domain in nscache:
                nscache[domain][nsDomain] = CacheEntry(expiration, True)
            else:
                entry = OrderedDict([(nsDomain, CacheEntry(expiration, True))])
                nscache[domain] = entry

    for ns in additional:
        if ns._type == RR.TYPE_A:
            insertToACache(ns)

#-------------------------------------------------------------------------------------------------------------------#
#                                                   Lookup code                                                     #
#-------------------------------------------------------------------------------------------------------------------#

#Handles data from response
def handleResponse(data, _id, cnames):
    (questions, answers, authorities, additional) = parseResponse(data, _id)
    
    if(len(answers) > 0):
        for answer in answers:
            if answer._type == RR.TYPE_CNAME: #if there are any cname records add it to list of cnames then find address 
                cnames.append((answer._dn, answer._cname, answer._ttl))
                return lookupDomain(answer._cname, cnames)
        for answer in answers:
            if answer._type == RR.TYPE_A: #Add a records add them to list then return, answer is found
                cnames.append((answer._dn, InetAddr.fromNetwork(answer._addr), answer._ttl))
        return cnames
    elif len(additional) > 0: #if there are no answers ask name servers
        for ns in additional:
            if ns._type == RR.TYPE_A:
                result = queryServer(questions[0]._dn, inet_ntoa(ns._addr), cnames)
                if result is not None:
                    return result

    else:
        nameServers = []
        for authority in authorities:
            if authority._type == RR.TYPE_NS:
                try:
                    a = lookupDomain(authority._nsdn, []) #try and get ip addresses for all the nameservers
                except NameError, timeout: #catch errors with server, doesn't matter as long as one gives us an answer
                    continue
                for i in a:
                    nameServers.append(i)
        if len(nameServers) == 0:
            raise LookupError #No nameservers repsponded
        for nameserver in nameServers:
            result = queryServer(questions[0]._dn,str(nameserver[1]), cnames)#query each nameserver and return if you get an answer
            if result is not None:
                return result
        

def queryServer(domain, serverAddress, cnames):
    timeNow = int(time())
    if (timeNow - requestReceived) > 60 - TIMEOUT: #check that you haven't been querying for more than 60 seconds
        raise timeout
    _id = randint(0, 65535) #random 16 bit int
    queryHeader = Header(_id, Header.OPCODE_QUERY, Header.RCODE_NOERR, 1).pack()
    question = QE(dn=domain).pack()
    packet = queryHeader + question
    cs.sendto(queryHeader + question, (serverAddress, 53))
    (data, address) = cs.recvfrom(512)
    return handleResponse(data, _id, cnames)

def getARecords(domain): #checks through acache for a domain 
    answers = []
    if domain in acache:
        expired = [] 
        entry = acache[domain]._dict
        for address, cache in entry.iteritems():
            if cache._expiration > int(time()):
                ttl = cache._expiration - int(time())
                answers.append((domain, address, ttl))
            else:
                expired.append(address) #cant delete from dict while iterating over it with iteritems so flag for deletion later
        for address in expired:
            del entry[address] #delete expried entries

    return answers

def lookupNameserver(ns): # lookup the ip addresses of a nameserver. very similar to getting a records just with an extra layer
    answers = []
    if ns in nscache:
        nservers = nscache[ns]
        toBeDeleted = []
        for nsDomain, cache in nservers.iteritems():
            if cache._expiration > int(time()):
                aRecords = getARecords(nsDomain)
                for a in aRecords:
                    answers.append(a)
            else:
                toBeDeleted.append[nsDomain]
        for i in toBeDeleted:
            del nservers[i]
    return answers
    

def lookupDomain(name, answers): #checks the cache for a domain name and if it cant find it starts querying name servers. Answers will be an empty list or contain all the previous c records
    records = getARecords(name)
    if len(records) > 0: # if a record found in cache return it
        for i in records:
            answers.append(i)
        return answers
    elif name in cnamecache: #if domain points to a cname resolve for domain it points to.
        entry = cnamecache[name]
        if entry._expiration > int(time()):
            ttl = entry._expiration - int(time())
            answers.append((name , entry._cname, ttl))
            return lookupDomain(entry._cname, answers)
        else:
            del cnamecache[name]
    else: #check though ns cache for nearest nameserver for the parent of domain we are looking for. 
        parent = name.parent()
        records = []
        while(len(records) == 0): 
            records = lookupNameserver(parent) #This will always find a nameserver because root name server is saved in cache and cant expire
            parent = parent.parent()
        for record in records:
            try:
                return queryServer(name, str(record[1]), answers) #recurively query server until domain is found
            except timeout: #ignore timeout as another nameserver may not time out
                continue
        raise timeout #all timed out so raise error

def getAuthority(domain): #checks the cache for the nameservers for a given domain. Should always get a value as this is called immediately after looking up the domain
    parent = domain.parent()
    if parent == None: #used incase the authority for root is requested, 
        parent = DomainName(".")
    records = []
    while len(records) == 0:  #check for nameserver for parent domain, if none found try the parent of that
        records = lookupNameserver(parent)
        if len(records) == 0:
            parent = parent.parent()
    authorities = []
    for dom in nscache[parent]: #find ip addresses of nameservers found
        if dom in acache:
            ttl = nscache[parent][dom]._expiration - int(time())
            authorities.append((parent, dom, ttl))

    return (authorities, records)

def resolve(domain): #finds domain then finds authority for that domain
    answers = lookupDomain(domain, [])
    if answers is None:
        raise NameError
    (authority, additional) = getAuthority(answers[-1][0])
    return (answers, authority, additional)

def constructPacket(err, data, question, qid): # creates the packet from data, data is a three tuple of lists ([answer], [authroity], [additional])
    header = Header(qid, Header.QUERY, err, 1, len(data[0]), len(data[1]), len(data[2]), True)
    packet = header.pack()
    packet += question.pack()
    for i in data[0]:
        if i[1].__class__.__name__ == 'DomainName':
            packet += RR_CNAME(i[0], i[2], i[1]).pack()
        else:
            packet += RR_A(i[0], i[2], i[1].toNetwork()).pack()
    for i in data[1]:
        packet += RR_NS(i[0], i[2], i[1]).pack()
    for i in data[2]:
        packet += RR_A(i[0], i[2], i[1].toNetwork()).pack()
    return packet


# This is a simple, single-threaded server that takes successive
# connections with each iteration of the following loop:
requestReceived = 0
while 1:
    (data, address,) = ss.recvfrom(512)  # DNS limits UDP msgs to 512 bytes
    requestReceived = int(time())
    if not data:
        log.error("client provided no data")
        continue
    try:
        (queryId, queries) = parseRequest(data)
    except NotImplementedError:
        continue
  
    print "Received query: " + str(queries[0])
    requestDomain = queries[0]._dn
    results = ([],[],[])
    try:
        results = resolve(requestDomain)
        error = Header.RCODE_NOERR
    except NameError:
        error = Header.RCODE_NAMEERR
    except timeout:
        error = Header.RCODE_SRVFAIL
    except AttributeError:
        error = Header.RCODE_SRVFAIL
    except LookupError:
        error = Header.RCODE_SRVFAIL
    except ValueError:
        error = Header.RCODE_FORMATERR

    reply = constructPacket(error, results, queries[0], queryId)
#
# TODO: Insert code here to perform the recursive DNS lookup;
#       putting the result in reply.
#
    # logger.log(DEBUG1, "our reply in full:")
    # logger.log(DEBUG1, hexdump(reply))

    ss.sendto(reply, address)
