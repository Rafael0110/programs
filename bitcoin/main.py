# -*- coding: utf-8 -*-

from zaifapi import ZaifPublicApi  # Zaifが公開している認証情報が要らないAPIを実行するクラス
from pprint import pprint  # 表示用(jsonをきれいに表示してくれる)
from time import sleep

if __name__ == '__main__':
    zaif = ZaifPublicApi()

    print('---last_price : 終値--')
    pprint(zaif.last_price('btc_jpy'))

    print('---ticker : ティッカー（集計情報取得）--')
    pprint(zaif.ticker('btc_jpy'))

    print('---trades : 全ての取引履歴--')
    print('取得件数：' + str(len(zaif.trades('btc_jpy'))))
    pprint(zaif.trades('btc_jpy'))

    print('---depth : 板情報--')
    print('取得件数[買い]：' + str(len(zaif.depth('btc_jpy')['asks'])))
    print('取得件数[売り]：' + str(len(zaif.depth('btc_jpy')['bids'])))
    pprint(zaif.depth('btc_jpy'))

    print('---currency_pairs : trade_history等で利用可能な通貨ペア情報--')
    pprint(zaif.currency_pairs('btc_jpy'))

    print('---currencies : deposit_history等で利用可能な通貨情報--')
    pprint(zaif.currencies('all'))