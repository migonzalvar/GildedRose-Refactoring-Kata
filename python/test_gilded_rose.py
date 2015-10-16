# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_decrementa_sellin_y_quality(self):
        ''' hola mundo  '''
        items = [Item("any name", 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_decrementa_doble_tras_vencimiento(self):
        items = [Item("any name", 0, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(1, items[0].quality)

    def test_la_quality_nunca_es_negativa(self):
        items = [Item("any name", 2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEquals(0, items[0].quality)

    def test_aged_brie_incrementa_quality(self):
        items = [Item("Aged Brie", 2, 1)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEquals(2, items[0].quality)

    def test_la_quality_nunca_es_mas_de_50(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEquals(50, items[0].quality)

    def test_sulfuras_nunca_se_vende_ni_baja_la_calidad(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 5)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEquals(5, items[0].quality)
        self.assertEquals(2, items[0].sell_in)

    def test_conjured_degrada_el_doble_que_el_resto(self):
        items = [Item("Conjured Mana Cake", 2, 5)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEquals(3, items[0].quality)

if __name__ == '__main__':
    unittest.main()
