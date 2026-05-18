package com.blueur.demotory;

import java.util.Map;

import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.map.IMap;

import lombok.extern.slf4j.Slf4j;

import io.micrometer.core.instrument.MeterRegistry;
import io.micrometer.core.instrument.Gauge;
import io.micrometer.core.instrument.Counter;

@Slf4j
@Controller
public class RootController {
  @Autowired
  private HazelcastInstance hazelcastInstance;

  private final Counter mapChangesCounter;

  @Autowired
  public RootController(MeterRegistry meterRegistry) {
    // Gauge: nombre d'entrées dans la map
    Gauge.builder("demotory_map_entries", this, ctrl -> ctrl.entriesMap().size())
         .description("Nombre d'entrées dans la map Hazelcast")
         .register(meterRegistry);

    // Counter: nombre de changements dans la map
    this.mapChangesCounter = meterRegistry.counter("demotory_map_changes_total");
  }

  private IMap<String, String> entriesMap() {
    return hazelcastInstance.getMap("entries");
  }

  @GetMapping
  public String index(Model model) {
    final Map<String, String> entries = entriesMap().getAll(entriesMap().keySet());
    model.addAttribute("entries", entries);
    model.addAttribute("entry",
        new Entry(RandomStringUtils.randomAlphanumeric(2), RandomStringUtils.randomAlphanumeric(4)));
    return "index";
  }

  @PostMapping
  public String put(@ModelAttribute Entry entry) {
    entriesMap().put(entry.getKey(), entry.getValue());
    mapChangesCounter.increment();
    log.info("Put {}={}", entry.getKey(), entry.getValue());
    return "redirect:.";
  }

  @DeleteMapping("/{key}")
  public String delete(@PathVariable String key) {
    entriesMap().delete(key);
    mapChangesCounter.increment();
    log.info("Delete {}", key);
    return "redirect:.";
  }
}
