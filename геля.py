 for c in all_computers:
      values = [str(c.ID), c.name, c.brand,c.processor, c.videocard, str(c.RAM), str(c.SSD), str(c.weight)  str(c.price),str(c.instock)]

      if a in values and b in values:
        print(c.name, c.brand, c.processor)
