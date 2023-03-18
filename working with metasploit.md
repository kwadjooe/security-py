## Working with Metasploit  
---
    msfdb init  >> intialize the metasploit database
    msfconsole  >> to start 
    db_status  >> get the database status
    db_connection -h  >> to get 
    db_nmap  >> to start the Nmap module inside msfconsole  
    db_disconect  >> to disconnect the database  
    db_import  >> import results from other tools such as Nessus, Nmap ...   
    db_rebuild_cache  >> Rebuild the cache if the earlier cache gets corrupted or is stored with older results  
    db_remove  >> Removes the saved data service entry  
    db_save  >> Saves the current data service entry as the default  

## Working with Workspace  
---
    workspace -h  >> get help on workspace  
    workspace   >> List workspaces  
    workspace -v  >> List workspaces verbosely  
    workspace [name]  switch workspace  
    workspace -a [name]  >> Add workspace  
    workspace -d [name]  >> Delete workspace
    workspace -D  >> Delete all workspace  
    workspace -r <old> <new>  Rename workspace  

---
## Port Scanning with Metasploit  

---
    db_nmap -Pn 10.X.X.X
    db_nmap -sV 10.X.X.X
    db_nmap -Pn -p3389 10.X.X.X  
    db_nmap -Pn -p445 --script smb-os-discovery 10.X.X.X  
    db_nmap -Pn -p445 --script smb-vuln-ms17-010 10.X.X.X  

- Searching for CVE  
 search cve:2021 type:exploit  
