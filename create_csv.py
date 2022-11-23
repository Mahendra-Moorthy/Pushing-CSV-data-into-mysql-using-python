import csv
header = ['Name', 'Terraform', 'Kubernetes', 'Ansible']
data = [
    ['Mahendra', 4, 3, 2],
    ['Aleks', 5, 5, 5],
    ['Ilja jantikovs', 5, 5, 4]
]
with open('Internlist.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
