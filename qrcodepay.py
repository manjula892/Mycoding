import qrcode
x=qrcode.QRCode()
upi_id="xxxxxxxxxxxxxxxxxxxxx"
name="Learn With manjula"
note="Just for coffee"
amount="100"
Link=f"upi://pay?pa={upi_id}&pn={name}&tn={note}&am={amount}&cu=INR"
x.add_data(Link)
x.make(fit=True)
res = x.make_image(fill_color="black", back_color="white")
res.save("pay.png")
print("created!!!")