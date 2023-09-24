# Steganography HW

HW1 for NCKU INFORMATION SECURITY 2023

A python program to hide chinese sentence with steganography.

It encodes text by generating sentences for each character in cleartext. Each sentence will end in ！, 。, or ？, and having random amount of commas (、 or ，), the amount of comma in a sentence shows where the cleartext is.

For example, if the first sentence has no comma, the cleartext is the first character, and if the second sentence has one comma, it's the second character.

> 你召酒厥佾我渙蝙患吮。此好稚鈐鶯踝菱姜古，脣黷簾腸蠔臆妻斂烊。

The above sentence will be decoded as 你好 (Hello)

## Prerequisites

- Have `python` or `python3` installed

## How to use

- `git clone` this project
- `python3 main.py`
- Enter the cleartext

Then the screen will show the cipher text and the cleartext it got from decoding

## Example

```
Enter the cleartext : 在成年禮以後見我

加密結果：
衙，暮先、攫梁、足，在部，呆桀、佇尷，餛襯員計喪匾淮淺、晉，苞、嬪？玲詢鄱膳涉顯鳥成黷液穩梧詔譁盡戴槨祠鰓莢蹼奈，閏鏑硯，彗萵，嬪，兜喉徇、速獗檻宰、得獐佞，皈！孫毗急肩，葛止榷，起、墊惠，年讀霄徘焚施、腥望，砸，榷用神嗽俾寫贊未渦抬，桐屁燃戛噬畜仞桑，慣、崁眾殊、擲落蔑碌管，飄，烊揪插礬，肪黯！銜墳幗鞣捉鈉、購召酒厥，聶溉落、視禮彈磊、崢蹊什坑痘輾枸，刈、盧歹、鹼囈喉，晏，俺，祠蜥途娣、溪編拄、饜隻秤軔謊伶晴邊地椅乩，枴膺，組爪，鼬猙許，辣窯奸，渠。率，秦、杳、珠、以皆框莉蜴擎條罈穹粒釣姒蟬蠕尼閘燭吻、逼，擲震聆瞻毓稚鈐鶯踝菱姜古，脣黷簾腸蠔臆妻斂烊，牠。柬票剁鄱嘆憔捆、鉤寮幢、蒂後釣滌，託糠、劉、及認獅、咕羌弄怖、蜿單，饜多，淺掛隕、蒸筵、瘩、酗半梢第，註識瓢。愿鋪，貌，電簞邁菲，冷淒噙僵德見、箴、屜耕噬裸表、堪韓、宛禍醃遮，貉恆、淫，嘯胸璩涉粳撻臭、腑、鍰、鏑訛酵閱、蘇、官氳寢？假那固，佾我渙蝙患吮，諦捲、胛扉搬，嬸纜耙雅腆痰靼啣諄窘跪眨、妾戊垂慧洪顆建群浪萄兄蠔鈣倥。

解密結果：
在成年禮以後見我
```

## Note

- Trying to encode text with comma will make decoding fail
- This program is meant to encode chinese characters
