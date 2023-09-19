import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('example.xml')
root = tree.getroot()

# Iterate through each <paymentItem> element
for payment_item in root.findall('.//paymentItem'):
    # Check if <originalQuantity> element exists
    original_quantity_element = payment_item.find('originalQuantity')
    if original_quantity_element is None:
        # If <originalQuantity> is missing, create it with a value of 0
        original_quantity_element = ET.Element('originalQuantity')
        original_quantity_element.text = '0'
        
        # Find the <completedQuantity> element
        completed_quantity_element = payment_item.find('completedQuantity')
        
        # Insert <originalQuantity> before <completedQuantity>
        payment_item.insert(list(payment_item).index(completed_quantity_element), original_quantity_element)

# Save the updated XML file
tree.write('updated-filename.xml')
