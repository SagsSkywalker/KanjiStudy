package com.wandererraven.mltest

import android.content.Context
import android.os.Parcel
import android.os.Parcelable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.ImageView
import android.widget.TextView

class KanjiListElement(): Parcelable{
    var kunyomi: String = ""
    var onyomi: String = ""
    var meaning: String = ""
    var image: Int = R.mipmap.select_kanji
    var kanji: String = ""

    constructor(parcel: Parcel) : this() {
        kunyomi = parcel.readString()
        onyomi = parcel.readString()
        meaning = parcel.readString()
        image = parcel.readInt()
        kanji = parcel.readString()
    }

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeString(kunyomi)
        parcel.writeString(onyomi)
        parcel.writeString(meaning)
        parcel.writeInt(image)
        parcel.writeString(kanji)
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<KanjiListElement> {
        override fun createFromParcel(parcel: Parcel): KanjiListElement {
            return KanjiListElement(parcel)
        }

        override fun newArray(size: Int): Array<KanjiListElement?> {
            return arrayOfNulls(size)
        }
    }

}

class KanjiListAdapter(private val context: Context, private val dataSource: ArrayList<KanjiListElement>): BaseAdapter(){
    private val inflater: LayoutInflater = context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val rowView = inflater.inflate(R.layout.kanji_list_element, parent, false)
        //Declarar vistas
        val image = rowView.findViewById(R.id.img_list_kanji_element_image) as ImageView
        val meaning = rowView.findViewById(R.id.txt_list_kanji_element_meaning) as TextView
        val kunyomi = rowView.findViewById(R.id.txt_list_kanji_element_kun) as TextView
        val onyomi = rowView.findViewById(R.id.txt_list_kanji_element_on) as TextView
        val kanji = rowView.findViewById(R.id.txt_list_kanji_element_kanji) as TextView
        //Armar el Kanji Element
        val kanjiElement = getItem(position) as KanjiListElement
        image.id = kanjiElement.image
        meaning.text = kanjiElement.meaning
        kunyomi.text = kanjiElement.kunyomi
        kanji.text = kanjiElement.kanji
        onyomi.text = kanjiElement.onyomi
        return rowView
    }

    override fun getItem(position: Int): Any {
        return dataSource[position]
    }

    override fun getItemId(position: Int): Long {
        return position.toLong()
    }

    override fun getCount(): Int {
        return dataSource.size
    }
}