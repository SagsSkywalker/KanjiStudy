package com.wandererraven.mltest

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.os.Parcel
import android.os.Parcelable
import kotlinx.android.synthetic.main.activity_main_menu.*

class MainMenu : AppCompatActivity() {

    val listKanjis = arrayListOf<KanjiListElement>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main_menu)

        val kanjiElement: KanjiListElement = KanjiListElement()
        kanjiElement.image = R.mipmap.selectKanji
        kanjiElement.kunyomi = "いち"
        kanjiElement.meaning = "one"
        val kanjiElement2: KanjiListElement = KanjiListElement()
        kanjiElement.image = R.mipmap.selectKanji
        kanjiElement.kunyomi = "に"
        kanjiElement.meaning = "two"
        listKanjis.add(kanjiElement2)
        val kanjiElement3: KanjiListElement = KanjiListElement()
        kanjiElement.image = R.mipmap.selectKanji
        kanjiElement.kunyomi = "さん"
        kanjiElement.meaning = "three"
        listKanjis.add(kanjiElement3)
        val adapter = KanjiListAdapter(this, listKanjis)
        lst_kanjis.adapter = adapter
    }


}

class KanjiElements():Parcelable{
    var listKanjis: List<KanjiListElement> = arrayListOf<KanjiListElement>()

    constructor(parcel: Parcel) : this() {
        listKanjis = parcel.createTypedArrayList(KanjiListElement)
    }

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeTypedList(listKanjis)
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<KanjiElements> {
        override fun createFromParcel(parcel: Parcel): KanjiElements {
            return KanjiElements(parcel)
        }

        override fun newArray(size: Int): Array<KanjiElements?> {
            return arrayOfNulls(size)
        }
    }
}
