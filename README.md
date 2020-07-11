# pyawabi

`pyawabi` is a python warapper for awabi(https://github.com/nakagami/awabi).

## Requirements

- Rust https://www.rust-lang.org/learn/get-started
- setuptools-rust https://pypi.org/project/setuptools-rust/
- MeCab dictionary https://github.com/nakagami/awabi#requirements-and-how-to-install

## Install

```
$ pip install setuptools-rust
$ pip install pyawabi
```

## Example

```
>>> import pyawabi
>>> import pprint
>>> pp = pprint.PrettyPrinter()
>>> pp.pprint(pyawabi.awabi.tokenize("すもももももももものうち"))
[('すもも', '名詞,一般,*,*,*,*,すもも,スモモ,スモモ'),
 ('も', '助詞,係助詞,*,*,*,*,も,モ,モ'),
 ('もも', '名詞,一般,*,*,*,*,もも,モモ,モモ'),
 ('も', '助詞,係助詞,*,*,*,*,も,モ,モ'),
 ('もも', '名詞,一般,*,*,*,*,もも,モモ,モモ'),
 ('の', '助詞,連体化,*,*,*,*,の,ノ,ノ'),
 ('うち', '名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ')]
>>> pp.pprint(pyawabi.tokenize_n_best("すもももももももものうち", 2))
[[('すもも', '名詞,一般,*,*,*,*,すもも,スモモ,スモモ'),
  ('も', '助詞,係助詞,*,*,*,*,も,モ,モ'),
  ('もも', '名詞,一般,*,*,*,*,もも,モモ,モモ'),
  ('も', '助詞,係助詞,*,*,*,*,も,モ,モ'),
  ('もも', '名詞,一般,*,*,*,*,もも,モモ,モモ'),
  ('の', '助詞,連体化,*,*,*,*,の,ノ,ノ'),
  ('うち', '名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ')],
 [('すもも', '名詞,一般,*,*,*,*,すもも,スモモ,スモモ'),
  ('も', '助詞,係助詞,*,*,*,*,も,モ,モ'),
  ('もも', '名詞,一般,*,*,*,*,もも,モモ,モモ'),
  ('もも', '名詞,一般,*,*,*,*,もも,モモ,モモ'),
  ('も', '助詞,係助詞,*,*,*,*,も,モ,モ'),
  ('の', '助詞,連体化,*,*,*,*,の,ノ,ノ'),
  ('うち', '名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ')]]
>>>
```
