# Warmup

### 1

|  Query |  Result  |
| ------ | -------- |
| dig @199.19.56.1 www.xorp.org +norecurse   |  ;; QUESTION SECTION:<br>;www.xorp.org.			IN	A<br><br>;; AUTHORITY SECTION:<br>xorp.org.		86400	IN	NS	ns.xorp.org.<br>xorp.org.		86400	IN	NS	ns2.xorp.org.<br><br>;; ADDITIONAL SECTION:<br>ns.xorp.org.		86400	IN	A	128.16.70.254<br>ns2.xorp.org.		86400	IN	A	193.63.58.145|
| dig @193.63.58.145 www.xorp.org +norecurse   |  ;; QUESTION SECTION:<br>;www.xorp.org.			IN	A<br><br>;; ANSWER SECTION:<br>www.xorp.org.		3600	IN	A	208.74.158.171<br><br>;; AUTHORITY SECTION:<br>xorp.org.		3600	IN	NS	ns2.xorp.org.<br>xorp.org.		3600	IN	NS	ns.xorp.org.<br><br>;; ADDITIONAL SECTION:<br>ns.xorp.org.		3600	IN	A	128.16.70.254<br>ns2.xorp.org.		3600	IN	A	193.63.58.145|
