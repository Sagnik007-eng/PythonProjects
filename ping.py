import subprocess

l=['ping -n 1 8.8.8.8','ping -n 1 6.7.8.8','ping -n 1 8.8.4.4','ping -n 1 1.1.1.1']
for i in l:
  try:
      output = subprocess.check_output(i.split())
      #command = f'ping -1 {i}'

      print(output.decode())
  except Exception as e:
      print(f'{i} is unreachable')
