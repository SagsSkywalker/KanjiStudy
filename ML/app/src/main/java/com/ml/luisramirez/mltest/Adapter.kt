package com.ml.luisramirez.mltest

import android.content.Context
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView


class Adapter(internal var context: Context, internal var items: Array<String>) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {
    internal var roma = arrayOf("ichi", "ni", "san", "yon")
    internal var mean = arrayOf("One", "Two", "Three", "Four")

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inflater = LayoutInflater.from(context)
        val row = inflater.inflate(R.layout.custome_row, parent, false)
        return Item(row)
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        //((Item) holder).imgView.setImageDrawable(ContextCompat.getDrawable(R.drawable.track));
        (holder as Item).txtRomaji.text = roma[position]
        holder.txtMeaning.text = mean[position]
    }

    override fun getItemCount(): Int {
        return items.size
    }

    inner class Item(itemView: View) : RecyclerView.ViewHolder(itemView) {
        internal var txtRomaji: TextView
        internal var txtMeaning: TextView
        internal var imgView: ImageView

        init {
            txtRomaji = itemView.findViewById<View>(R.id.txtRomaji) as TextView
            txtMeaning = itemView.findViewById<View>(R.id.txtMeaning) as TextView
            imgView = itemView.findViewById<View>(R.id.imgKanji) as ImageView
        }
    }
}
