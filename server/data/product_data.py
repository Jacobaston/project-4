from models.product import Product

list_product = [
    Product(
        product_name="White Trainers",
        product_image="https://i.ibb.co/0YkH1Px/pumatrainers.jpg",
        brand="Puma",
        size="8",
        description="White Puma trainers - only used a few times",
        category="Shoes",
        price=20.00,
        condition="Worn occasionally - good condition",
        in_stock=False,
        gender="Unisex",
        user_id=1
    ),
    Product(
        product_name="Khaki Dress",
        product_image="https://i.ibb.co/Chj30XW/khakidress.jpg",
        brand="Zara",
        size="12",
        description="Khaki coloured dress - never worn",
        category="Dresses",
        price=20.00,
        condition="Brand new with tags",
        in_stock=False,
        gender="Womens",
        user_id=1
    ),
    Product(
        product_name="Wooly jacket",
        product_image="https://i.ibb.co/QnyZSc8/woolcoat.jpg",
        brand="Zara",
        size="12",
        description="Teddy bear-like jacket from Zara with big pockets",
        category="Outerwear",
        price=25.00,
        condition="New without tags",
        in_stock=True,
        gender="Womens",
        user_id=1
    ),
    Product(
        product_name="Cowboy Boots",
        product_image="https://i.ibb.co/Jcx2L7G/cowboyboots.jpg",
        brand="Sendra",
        size="7",
        description="Cowboy boots in size 7",
        category="Shoes",
        price=35.00,
        condition="Worn occasionally - good condition",
        in_stock=True,
        gender="Womens",
        user_id=1
    ),
    Product(
        product_name="Nike socks",
        product_image="https://i.ibb.co/VWGDGdw/nikesocks.jpg",
        brand="Nike",
        size="8",
        description="Black ankle socks",
        category="Other",
        price=5.00,
        condition="Worn often - some damage/wear",
        in_stock=False,
        gender="Unisex",
        user_id=2
    ),
    Product(
        product_name="Leather jacket",
        product_image="https://i.ibb.co/Tgf1c33/leatherjacket.jpg",
        brand="All Saints",
        size="M",
        description="Biker jacket",
        category="Outerwear",
        price=155.00,
        condition="New without tags",
        in_stock=True,
        gender="Womens",
        user_id=2
    ),
    Product(
        product_name="North Face T-shirt",
        product_image="https://i.ibb.co/864XxLT/northfacetee.jpg",
        brand="North Face",
        size="Large",
        description="Blue North Face T-shirt with logo on the front and back",
        category="Tops",
        price=11.99,
        condition="New without tags",
        in_stock=True,
        gender="Mens",
        user_id=2
    ),
    Product(
        product_name="Black jeans",
        product_image="https://i.ibb.co/LZZxXmV/blackjeans.jpg",
        brand="Pull & Bear",
        size="32 Regular",
        description="Black slim fit jeans",
        category="Bottoms",
        price=14.99,
        condition="Worn often - some damage/wear",
        in_stock=True,
        gender="Mens",
        user_id=2
    ),
    Product(
        product_name="Grey oversize hoodie",
        product_image="https://i.ibb.co/s1kTbwh/greyhoodie.jpg",
        brand="Ralph Lauren",
        size="Large",
        description="Grey oversized Ralph Lauren hoddie with large logo on the front",
        category="Tops",
        price=34.99,
        condition="Worn occasionally - good condition",
        in_stock=False,
        gender="Mens",
        user_id=2
    ),
    Product(
        product_name="White t-shirt",
        product_image="https://i.ibb.co/rMyPDLS/whiteteeshirt.jpg",
        brand="Zara",
        size="12 ",
        description="Plain white t-shirt",
        category="Tops",
        price=5.00,
        condition="Worn occasionally - good condition",
        in_stock=False,
        gender="Womens",
        user_id=3
    ),

    Product(
        product_name="Red jumper",
        product_image="https://i.ibb.co/1mnbSfy/redjumper.jpg",
        brand="Zara",
        size="12",
        description="Super cosy red jumper",
        category="Tops",
        price=30.50,
        condition="Worn often - some damage/wear",
        in_stock=True,
        gender="Womens",
        user_id=3
    ),
    Product(
        product_name="Black Dress",
        product_image="https://i.ibb.co/PCsxRjQ/blackdress.jpg",
        brand="Ted Baker",
        size="12",
        description="Little black dress",
        category="Dresses",
        price=50.00,
        condition="Worn often - some damage/wear",
        in_stock=True,
        gender="Womens",
        user_id=2
    ),
    Product(
        product_name="Light blue jeans",
        product_image="https://i.ibb.co/74W0xXR/bluejeans.jpg",
        brand="Topshop",
        size="12 Long",
        description="Topshop tall jeans - very worn (may have a couple of holes)",
        category="Trousers",
        price=5.00,
        condition="Worn occasionally - good condition",
        in_stock=True,
        gender="Womens",
        user_id=1
    ),
    Product(
        product_name="New York baseball cap",
        product_image="https://i.ibb.co/F07m8x8/baseballcap.jpg",
        brand="New Era",
        size="One size fits all",
        description="Black New York Yankies cap",
        category="Other",
        price=20.00,
        condition="Worn occasionally - good condition",
        in_stock=False,
        gender="Unisex",
        user_id=3
    ),
        Product(
        product_name="Unworn Calvin Klein boxers - three pack",
        product_image="https://i.ibb.co/qpdZbsj/boxers.jpg",
        brand="Calvin Klien",
        size="Large",
        description="Three pairs of black CK boxers in box - unopened",
        category="Underwear",
        price=20.00,
        condition="Worn often - some damage/wear",
        in_stock=True,
        gender="Mens",
        user_id=2
    ),
    Product(
        product_name="Michael Kors brown handbag",
        product_image="https://i.ibb.co/1mYNK4C/handbag.jpg",
        brand="Michael Kors",
        size="Large",
        description="Brown large MK handbag",
        category="Accessories",
        price=20.00,
        condition="Brand new with tags",
        in_stock=True,
        gender="Womens",
        user_id=1
    ),
    Product(
        product_name="Mango long silver necklace",
        product_image="https://i.ibb.co/CMY40Kg/necklace.jpg",
        brand="Mango",
        size="n/a",
        description="Long silver necklace with jewel on end",
        category="Other",
        price=12.00,
        condition="New without tags",
        in_stock=True,
        gender="Womens",
        user_id=3
    ),
    Product(
        product_name="Victoria's Secret Bra",
        product_image="https://i.ibb.co/ccy3m7D/bra.jpg",
        brand="Victoria's Secret",
        size="32C",
        description="Black unworn bra",
        category="Lingerie",
        price=30.00,
        condition="New without tags",
        in_stock=True,
        gender="Womens",
        user_id=3
    )
]