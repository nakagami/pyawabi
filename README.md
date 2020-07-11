# pyawabi

`pyawabi` is a python warapper for awabi(https://github.com/nakagami/awabi).

## How to build and use module

It needs nightly Rust becauese using PyO3 https://github.com/PyO3/pyo3 .

Let's cargo build and copy `libpyawabi.so` to somewhere python path as pyawabi.so .
```
$ git clone https://github.com/nakagami/pyawabi.git
$ cd pyawabi
$ cargo build --release
$ cd target/release
$ cp libawabi.so /some/where/python-project/awabi.so
```

## Example

```
>>> import awabi
>>> import pprint
>>> pp = pprint.PrettyPrinter()
>>> pp.pprint(awabi.tokenize("すもももももももものうち"))
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
