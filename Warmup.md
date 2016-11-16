# Warmup

### 1

| Query                                    | Result                                   |
| ---------------------------------------- | ---------------------------------------- |
| dig @199.19.56.1 www.xorp.org +norecurse | ;; QUESTION SECTION:<br>;www.xorp.org.			IN	A<br><br>;; AUTHORITY SECTION:<br>xorp.org.		86400	IN	NS	ns2.xorp.org.<br><br>;; ADDITIONAL SECTION:<br>ns2.xorp.org.		86400	IN	A	193.63.58.145 |
| dig @193.63.58.145 www.xorp.org +norecurse | ;; QUESTION SECTION:<br>;www.xorp.org.			IN	A<br><br>;; ANSWER SECTION:<br>www.xorp.org.		3600	IN	A	208.74.158.171<br><br>;; AUTHORITY SECTION:<br>xorp.org.		3600	IN	NS	ns2.xorp.org.<br><br>;; ADDITIONAL SECTION:<br>ns2.xorp.org.		3600	IN	A	193.63.58.145 |

### 2

| Query                                    | Result                                   |
| ---------------------------------------- | ---------------------------------------- |
| dig @198.41.0.4 newgate.cs.ucl.ac.uk +norecurse | ;; QUESTION SECTION:<br>;newgate.cs.ucl.ac.uk.		IN	A<br><br>;; AUTHORITY SECTION:<br>uk.			172800	IN	NS	nsa.nic.uk.<br><br>;; ADDITIONAL SECTION:<br>nsa.nic.uk.		172800	IN	A	156.154.100.3 |
| dig @156.154.100.3 newgate.cs.ucl.ac.uk +norecurse | ;; QUESTION SECTION:<br>;newgate.cs.ucl.ac.uk.		IN	A<br><br>;; AUTHORITY SECTION:<br> ac.uk.			172800	IN	NS	ns0.ja.net. |
| dig @198.41.0.4 ns0.ja.net +norecurse    | ;; QUESTION SECTION:<br>;ns0.ja.net.			IN	A<br><br>;; AUTHORITY SECTION:<br>net.			172800	IN	NS	a.gtld-servers.net.<br><br>;; ADDITIONAL SECTION:<br>a.gtld-servers.net.	172800	IN	A	192.5.6.30 |
| dig @192.5.6.30 ns0.ja.net +norecurse    | ;; QUESTION SECTION:<br>;ns0.ja.net.			IN	A<br><br>;; AUTHORITY SECTION:<br>ja.net.			172800	IN	NS	ns0.ja.net.<br><br>;; ADDITIONAL SECTION:<br>ns0.ja.net.		172800	IN	A	128.86.1.20 |
| dig @128.86.1.20 ns0.ja.net +norecurse   | ;; QUESTION SECTION:<br>;ns0.ja.net.			IN	A<br><br>;; ANSWER SECTION:<br>ns0.ja.net.		86400	IN	A	128.86.1.20<br><br>;; AUTHORITY SECTION:<br>ja.net.			86400	IN	NS	ns0.ja.net. |
| dig @128.86.1.20 newgate.cs.ucl.ac.uk +norecurse | ;; QUESTION SECTION:<br>;newgate.cs.ucl.ac.uk.		IN	A<br><br>;; ANSWER SECTION:<br>newgate.cs.ucl.ac.uk.	86400	IN	A	128.16.9.83<br><br>;; AUTHORITY SECTION:<br>cs.ucl.ac.uk.		360000	IN	NS	ns0.ja.net.<br><br>;; ADDITIONAL SECTION:<br>ns0.ja.net.		86400	IN	A	128.86.1.20 |

| Query                                    | Result                                   |
| ---------------------------------------- | ---------------------------------------- |
| dig @198.41.0.4 www.microsoft.com +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com.		IN	A<br><br>;; AUTHORITY SECTION:<br>com.			172800	IN	NS	e.gtld-servers.net.<br><br>;; ADDITIONAL SECTION:<br>e.gtld-servers.net.	172800	IN	A	192.12.94.30 |
| dig @192.12.94.30 www.microsoft.com +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com.		IN	A<br><br>;; AUTHORITY SECTION:<br>microsoft.com.		172800	IN	NS	ns3.msft.net.<br><br>;; ADDITIONAL SECTION:<br>ns3.msft.net.		172800	IN	A	193.221.113.53 |
| dig @193.221.113.53 www.microsoft.com +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com.		IN	A<br><br>;; ANSWER SECTION:<br>www.microsoft.com.	3600	IN	CNAME	www.microsoft.com-c-2.edgekey.net. |
| dig @198.41.0.4 www.microsoft.com-c-2.edgekey.net. +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com-c-2.edgekey.net. IN	A<br><br>;; AUTHORITY SECTION:<br>net.			172800	IN	NS	e.gtld-servers.net.<br><br>;; ADDITIONAL SECTION:<br>ne.gtld-servers.net.	172800	IN	A	192.12.94.30 |
| dig @192.12.94.30 www.microsoft.com-c-2.edgekey.net. +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com-c-2.edgekey.net. IN	A<br><br>;; AUTHORITY SECTION:<br>edgekey.net.		172800	IN	NS	ns1-66.akam.net.<br><br>;; ADDITIONAL SECTION:<br>ns1-66.akam.net.	172800	IN	A	193.108.91.66 |
| dig @193.108.91.66 www.microsoft.com-c-2.edgekey.net. +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com-c-2.edgekey.net. IN	A<br><br>;; ANSWER SECTION:<br>www.microsoft.com-c-2.edgekey.net. 21600 IN CNAME www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. |
| dig @198.41.0.4 www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. IN A<br><br>;; AUTHORITY SECTION:<br>net.			172800	IN	NS	a.gtld-servers.net.<br><br>;; ADDITIONAL SECTION:<br>a.gtld-servers.net.	172800	IN	A	192.5.6.30 |
| dig @192.5.6.30 www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. IN A<br><br>;; AUTHORITY SECTION:<br>akadns.net.		172800	IN	NS	a3-129.akadns.net.<br><br>;; ADDITIONAL SECTION:<br>a3-129.akadns.net.	172800	IN	A	96.7.49.129 |
| dig @96.7.49.129 www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. +norecurse | ;; QUESTION SECTION:<br>;www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. IN A<br><br>;; ANSWER SECTION:<br>www.microsoft.com-c-2.edgekey.net.globalredir.akadns.net. 900 IN CNAME e2847.dspb.akamaiedge.net. |
| dig @198.41.0.4 e2847.dspb.akamaiedge.net. +norecurse | ;; QUESTION SECTION:<br>;e2847.dspb.akamaiedge.net.	IN	A<br><br>;; AUTHORITY SECTION:<br>net.			172800	IN	NS	a.gtld-servers.net.<br><br>;; ADDITIONAL SECTION:<br>a.gtld-servers.net.	172800	IN	A	192.5.6.30 |
| dig @192.5.6.30 e2847.dspb.akamaiedge.net. +norecurse | ;; QUESTION SECTION:<br>;e2847.dspb.akamaiedge.net.	IN	A<br><br>;; AUTHORITY SECTION:<br>akamaiedge.net.		172800	IN	NS	la1.akamaiedge.net.<br><br>;; ADDITIONAL SECTION:<br>la1.akamaiedge.net.	172800	IN	A	184.26.161.192 |
| dig @184.26.161.192 e2847.dspb.akamaiedge.net. +norecurse | ;; QUESTION SECTION:<br>;e2847.dspb.akamaiedge.net.	IN	A<br><br>;; AUTHORITY SECTION:<br>dspb.akamaiedge.net.	8000	IN	NS	n6dspb.akamaiedge.net.<br><br>;; ADDITIONAL SECTION:<br>n6dspb.akamaiedge.net.	8000	IN	A	23.3.15.50 |
| dig @23.3.15.50 e2847.dspb.akamaiedge.net. +norecurse | ;; QUESTION SECTION:<br>;e2847.dspb.akamaiedge.net.	IN	A<br><br>;; ANSWER SECTION:<br>e2847.dspb.akamaiedge.net. 20	IN	A	23.214.129.109 |

### 3

When querying for newgate.cs.ucl.ac.uk, nsa.nic.uk responded with ns0.ja.net. as the next server to query but did not have a glue record with the IP address for ns0.js.net. This meant going back to the root server to ask for this IP address before continuing the queries for the IP of newgate.cs.ucl.ac.uk

### 4

When querying for www.microsoft.com the answer given was a CNAME record for www.microsoft.com-c-2.edgekey.net. Further queries were required to find the IP of www.microsoft.com because a CNAME record means that www.microsoft.com points to the same IP address that www.microsoft.com-c-2.edgekey.net. points to. As it turned out www.microsoft.com-c-2.edgekey.net. also lead to a CNAME record so more queries had to be made to find the IP of the subsequent domain names.
