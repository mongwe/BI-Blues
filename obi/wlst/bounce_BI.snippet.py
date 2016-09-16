# ===================================================================
# Developed by RNM @ Rittman Mead
# Absolutely no warranty, use at your own risk
# Please include this header in any copy or reuse of the script you make
# ===================================================================#

# Restart BI Server
cd ('..')
cd ('oracle.biee.admin:oracleInstance=instance1,type=BIDomain.BIInstanceDeployment.BIComponent,biInstance=coreapplication,process=coreapplication_obis1,group=Service')

print 'Stopping the BI server'
params = jarray.array([], java.lang.Object)
signs = jarray.array([], java.lang.String)
invoke('stop', params, signs)

BIServerStatus = get('Status')
print 'BI ServerStatus : ' +BIServerStatus

print 'Starting the BI server'
params = jarray.array([], java.lang.Object)
signs = jarray.array([], java.lang.String)
invoke('start', params, signs)

BIServerStatus = get('Status')
print 'BI ServerStatus : ' +BIServerStatus

# Exit
exit()

