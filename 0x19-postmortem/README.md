THE FUALT AT A FACILITY

there was a outage of an intranet system at WEMEC FORENSIC INCOPORATIONS LIMITED which occurred at 11hrs and got resolved at 16hrs

The system was not listening on port 81 which led to all users being unable to access the system on their working points

The Nginx Server was inactive hence being unable to recieve requests or send reponses. So its settings were not well configured after they had a power outage for so long so it did not pick up

The issue was detected at 11:05 AM when one of the users attempted to access a service from the system
At 11:15 AM the Monitoring system detected a failure in the system and indicated that the system was down and later on it was escalated to me
At 11:30 the the investigations were started on finding out what cuased the system failure
at 12:10 Am the leading cuase was found  and i started working on it
At 12:30 AM the appropriate configurations for the nginx server were confiugured
At 12:45 AM the system was up and running, tests were conducted and completed at 13hrs

The main root cuase of the system failure was the inactive of the nginx server

