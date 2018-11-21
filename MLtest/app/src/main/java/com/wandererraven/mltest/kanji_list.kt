package com.wandererraven.mltest

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_kanji_list.*

class kanji_list : AppCompatActivity() {

    val listKanjis = arrayListOf<KanjiListElement>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_kanji_list)

        val kanjiElement: KanjiListElement = KanjiListElement()
        kanjiElement.image = R.mipmap.select_kanji
        kanjiElement.kanji = "一"
        kanjiElement.kunyomi = "ひと"
        kanjiElement.onyomi = "イチ"
        kanjiElement.meaning = "one"
        listKanjis.add(kanjiElement)
        val kanjiElement2: KanjiListElement = KanjiListElement()
        kanjiElement2.image = R.mipmap.select_kanji
        kanjiElement2.kanji = "二"
        kanjiElement2.kunyomi = "ふた"
        kanjiElement2.onyomi = "に"
        kanjiElement2.meaning = "two"
        listKanjis.add(kanjiElement2)
        val kanjiElement3: KanjiListElement = KanjiListElement()
        kanjiElement3.image = R.mipmap.select_kanji
        kanjiElement3.kanji = "三"
        kanjiElement3.kunyomi = "三つ"
        kanjiElement3.onyomi = "サン"
        kanjiElement3.meaning = "three"
        listKanjis.add(kanjiElement3)
        val adapter = KanjiListAdapter(this, listKanjis)
        lst_kanji_list.adapter = adapter

        lst_kanji_list.setOnItemClickListener{
            parent, view, position, id ->
            //Toast.makeText(this, listMarkers[position].titulo,Toast.LENGTH_SHORT).show()
            val detailActivity = Intent(applicationContext, kanji_detail::class.java)
            detailActivity.putExtra("kanjiElement",listKanjis[position])
            startActivity(detailActivity)
        }
    }
}
