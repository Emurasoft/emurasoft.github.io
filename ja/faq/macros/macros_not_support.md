# Q. マクロで JavaScript のあるメソッドを使うと、「オブジェクトでサポートされていないプロパティまたはメソッドです。」というエラーが表示されます。どうしてですか?

EmEditor では、最近の JavaScript/ECMAScript の多くの新しいメソッドは利用できません。EmEditor マクロは JScript 5.8 (Internet Explorer 8.0 に相当) を使用しているため、JScript 5.8 より後に追加された新しいメソッドは利用できません。また、置換表現で使用できる JavaScript は、Chakra (Microsoft Edge Legacy に相当) を使用しているため、ECMAScript 5.1 までをサポートしています。ECMAScript 5.1 より後に追加されたメソッドは利用できません。新しいメソッドを使用する前に、必須バージョンの要件を満たしているか確認してください。
