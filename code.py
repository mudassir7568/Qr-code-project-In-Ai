#pip install qrcode
#pip install pillow
import qrcode

#taking UPI id as input

upi_id = input("enter your UPI ID =")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment url based on the upi id and payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qrcode
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#save qrcode to image file

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytme_qr.png')
googlepay_qr.save('googlepay_qr.png')


#display qrcodes(install pillow library)

phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()
