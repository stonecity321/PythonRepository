#!/usr/bin/env python
#!/usr/bin/python
import cgi




reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

#form = cgi.FieldStorage()
#who = form['person'].value
#howmany = form['howmany'].value
print reshtml % ('abel', 'abel2', 'abel3')
form = cgi.FieldStorage()
print '<br/>form=',form
who = form['person'].value
howmany = form['howmany'].value
print "<br/>",who,howmany
